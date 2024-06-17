from cmath import nan
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter, defaultdict
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 8})
import os
import pandas as pd
import numpy as np
import math
import ast

dir = "data"
species = 5000
rows = 1
columns = 3

def plane(X, Y, P_NORM):
    Z = np.empty(np.shape(X.flatten()))

    for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):

        if ((1**P_NORM) - x**P_NORM - y**P_NORM) < 0:
            Z[i] = np.nan
        else:
            Z[i] = ((1**P_NORM) - x**P_NORM - y**P_NORM) ** (1/P_NORM)

    return np.reshape(Z, np.shape(X))

gammas = {"0305_133144":	[0.09353417, 0.03050835, 0.26988028],
"0305_133146":	[0.09786357, 0.35296366, 0.00866035],
"0305_133148":	[0.15816828, 0.09811163, 0.08356058],
"0305_133402":	[0.31130718, 0.44402908, 0.13832098],
"0305_142645":	[0.31931507, 0.50620181, 0.07760296],
"0305_191207":	[0.36965376, 0.39145762, 0.13208132],
"0305_191208":	[0.18512367, 0.05010743, 0.7647689 ],
"0805_144706":	[0.2374429 , 0.07744754, 0.68510957],
"0805_154609":	[0.21298414, 0.76816801, 0.01884785],
"0805_154611":	[0.46541916, 0.28869907, 0.24588177],
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


if __name__ == "__main__":

    for file_ID in p_norms.keys():

        df_strategies = pd.read_csv("{0}/{1}_strategies.csv".format(dir, file_ID))
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv("{0}/{1}_results.csv".format(dir, file_ID), index_col="time", header=0)

        fig = plt.figure()
        # fig.subplots_adjust(wspace=0, hspace=0)
        num_subplots = rows*columns
        timestep = int(np.max(df_abundances.index)/(num_subplots*100))*100

        for t in np.arange(timestep,  timestep*(num_subplots+1), timestep):
            loc = int(t/timestep)  
            ax = fig.add_subplot(rows, columns, loc, projection='3d')
            
            for ID in range(species):
                if bool(df_abundances.loc[t, "species" + str(ID)]) and not math.isnan(df_abundances.loc[t, "species" + str(ID)]):
                    alive = np.array(df_strategies.loc[ID, :].array)
                    ax.scatter(alive[0], alive[1], alive[2], c="gray", zorder=0, alpha=1, s=8)
                    ax.zorder

            ax.scatter(gammas[file_ID][0], gammas[file_ID][1], gammas[file_ID][2] , marker="*", zorder=1000, c="black")
            (x, y) = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
            z = plane(x, y, p_norms[file_ID])
            ax.plot_surface(x, y, z, color="lightgray", alpha=0.2, zorder=10000)
            ax.zorder
                    
            ax.set_xlim([0,1])
            ax.set_ylim([0,1])
            ax.set_zlim([0,1])
            # ax.invert_xaxis()
            ax.invert_yaxis()
            ax.set(xticklabels=[],
                yticklabels=[],
                zticklabels=[])
            ax.set_title(f"$t$={t}")
            

            # ax.title(t)
        plt.savefig(f"gammarandom_eta{file_ID}_Kmax5000_P{p_norms[file_ID]}_{rows}x{columns}.png", dpi=300)
        # plt.show()
        plt.clf()
            
