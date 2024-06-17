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
    
dir = "data_anim"
gammas = {"0305_133148": [0.15816828, 0.09811163, 0.08356058], 
        "0305_133402": [0.31130718, 0.44402908, 0.13832098],
        "0305_142645": [0.31931507, 0.50620181, 0.07760296], 
        "0805_144706": [0.2374429,  0.07744754, 0.68510957], 
        "0805_154611": [0.46541916, 0.28869907, 0.24588177],
        "0805_163442":	[0.48078824, 0.68576626, 0.21362533],
        "0805_171707":	[0.46876434, 0.74311983, 0.11392353],
        "0805_180041":	[0.57335855, 0.60717785, 0.20486727],
        "0805_180622":	[0.32561505, 0.10620694, 0.93951846],
        "0805_200753":	[0.26710816, 0.96337661, 0.02363751],
        "0905_104250":	[0.77524652, 0.48088468, 0.40956411]
}

p_norms = {"0305_133148": 0.5, 
        "0305_133402": 0.9,
        "0305_142645": 0.9, 
        "0805_144706": 1, 
        "0805_154611": 1,
        "0805_163442": 1.5,
        "0805_171707": 1.5,
        "0805_180041": 1.5,
        "0805_180622": 2,
        "0805_200753": 2,
        "0905_104250": 2
}

colors = {
    0.5: "#ff7d2d", 
    0.9: "#ff7d2d", 
    1: "#fac846", 
    1.1: "#a0c382", 
    1.5: "gray",
    2: "#a0c382"
}

species = 5000


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
            for ID in range(species):
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

        ani.save(f"anim_test_{file_ID}.mp4", fps=10, dpi=100)
        # plt.show()
