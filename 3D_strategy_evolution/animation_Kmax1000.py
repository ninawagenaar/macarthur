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
gammas = {"0905_102952":	[0.11111111, 0.11111111, 0.11111111],
"0905_102953":	[0.11111111, 0.11111111, 0.11111111],
"0905_102955":	[0.11111111, 0.11111111, 0.11111111],
"0905_102956":	[0.29502938, 0.29502938, 0.29502938],
"0905_103155":	[0.29502938, 0.29502938, 0.29502938],
"0905_103425":	[0.29502938, 0.29502938, 0.29502938],
"0905_103430":	[0.33333333, 0.33333333, 0.33333333],
"0905_103632":	[0.33333333, 0.33333333, 0.33333333],
"0905_103853":	[0.33333333, 0.33333333, 0.33333333],
"0905_103854":	[0.36834383, 0.36834383, 0.36834383],
"0905_104120":	[0.36834383, 0.36834383, 0.36834383],
"0905_104306":	[0.36834383, 0.36834383, 0.36834383],
"0905_104308":	[0.57735027, 0.57735027, 0.57735027],
"0905_104402":	[0.57735027, 0.57735027, 0.57735027],
"0905_104447":	[0.57735027, 0.57735027, 0.57735027]
}

p_norms = {"0905_102956": 0.9, 
"0905_103155": 0.9, 
"0905_103430": 1,
"0905_103632": 1,
"0905_103854": 1.1,
"0905_104120": 1.1,
"0905_104308": 2,
"0905_104402": 2
}

colors = {
    0.5: "#ff7d2d", 
    0.9: "#ff7d2d", 
    1: "#fac846", 
    1.1: "#a0c382", 
    2: "#a0c382"
}

def update_graph(num):
    ax.cla()
    data=df[df['time']==num]
    ax.scatter(gammas[file_ID][0], gammas[file_ID][1], gammas[file_ID][2], c="#233c4b", marker="*", zorder = 1)
    ax.scatter(data.x, data.y, data.z, c="gray", alpha=0.9, zorder=10)
    ax.plot_surface(x, y, z, color=planecolor, alpha=0.2, shade=False)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([0,1])
    ax.set(xticklabels=[],
                yticklabels=[],
                zticklabels=[])
    # ax.invert_xaxis()
    ax.invert_yaxis()
    # ax.invert_zaxis()

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
            for ID in range(1000):
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

        data=df[df['time']==0]
        graph = ax.scatter(data.x, data.y, data.z)
        (x, y) = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
        z = plane(x, y, p_norms[file_ID])
        planecolor = colors[p_norms[file_ID]]

        ani = matplotlib.animation.FuncAnimation(fig, update_graph, int(np.max(df['time'])), 
                                    interval=250, blit=False)

        ani.save(f"anim_test_{file_ID}.mp4", fps=10, dpi=300)
        # plt.show()