import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd
from collections import Counter, defaultdict
import math
import os

def plane(X, Y, P_NORM):
    Z = np.empty(np.shape(X.flatten()))

    for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):

        if ((1**P_NORM) - x**P_NORM - y**P_NORM) < 0:
            Z[i] = np.nan
        else:
            Z[i] = ((1**P_NORM) - x**P_NORM - y**P_NORM) ** (1/P_NORM)

    return np.reshape(Z, np.shape(X))

dir = "data"
gammas = {"0205_203057":	[0.21671153, 0.07068552, 0.62529199],
        "0205_203121":	[0.19851992, 0.71600003, 0.01756785],
        "0205_203122":	[0.41354574, 0.25652203, 0.21847695],
        "0205_203123":	[0.34835188, 0.49686732, 0.15478079],
        "0205_203150":	[0.35356888, 0.56050348, 0.08592764],
        "0205_203219":	[0.41385667, 0.43826782, 0.1478755 ],
        "0205_203220":	[0.22235491, 0.06018481, 0.91857579],
        "0205_203244":	[0.62423473, 0.52583956, 0.25065272],
        "0205_203313":	[0.02734706, 0.89386592, 0.28278329],
        "0205_203314":	[0.38692511, 0.27533206, 0.88004615],
        "0205_203349":	[0.86835016, 0.03263896, 0.49487644],
        "0205_203415":	[0.11232696, 0.49879536, 0.85941017]}

p_norms = {
"0205_203057": 0.9,
"0205_203123": 1,
"0205_203150": 1,
"0205_203220": 1.5,
"0205_203244": 1.5,
"0205_203314": 2,
"0205_203349": 2
}

colors = {
    0.5: "#ff7d2d", 
    0.9: "#ff7d2d", 
    1: "#fac846", 
    1.1: "#a0c382", 
    1.5: "lightgray",
    2: "#a0c382"
}

def update_graph(num):
    ax.cla()
    data=df[df['time']==num]
    ax.scatter(gammas[file_ID][0], gammas[file_ID][1], gammas[file_ID][2], c="#233c4b", marker="*")
    ax.scatter(data.x, data.y, data.z, c="gray", alpha=0.9)
    ax.plot_surface(x, y, z, color=planecolor, alpha=0.2, shade=False)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([0,1])
    # ax.invert_xaxis()
    ax.invert_yaxis()
    # ax.invert_zaxis()
    title.set_text('3D Test, time={}'.format(num))

if __name__ == "__main__":

    for file_ID in p_norms.keys():
        df_strategies = pd.read_csv("{0}/{1}_strategies.csv".format(dir, file_ID))
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv("{0}/{1}_results.csv".format(dir, file_ID), index_col="time", header=0)
        t = []
        x = []
        y = []
        z = []

        for time in np.arange(0, np.max(df_abundances.index), 100):
            for ID in range(500):
                if bool(df_abundances.loc[time, "species" + str(ID)]) and not math.isnan(df_abundances.loc[time, "species" + str(ID)]):
                    alive = np.array(df_strategies.loc[ID, :].array)
                    t.append(time/100)
                    x.append(alive[0])
                    y.append(alive[1])
                    z.append(alive[2])
        
        df = pd.DataFrame({"time": t ,"x" : x, "y" : y, "z" : z})


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set(xticklabels=[],
                yticklabels=[],
                zticklabels=[])
        title = ax.set_title('3D Test')
        data=df[df['time']==0]
        graph = ax.scatter(data.x, data.y, data.z)
        (x, y) = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
        z = plane(x, y, p_norms[file_ID])
        planecolor = colors[p_norms[file_ID]]
        

        ani = matplotlib.animation.FuncAnimation(fig, update_graph, int(np.max(df['time'])), 
                                    interval=250, blit=False)

        ani.save(f"anim_test_{file_ID}.mp4", fps=10, dpi=300)
        # plt.show()