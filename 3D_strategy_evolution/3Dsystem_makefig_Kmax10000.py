from cmath import nan
import matplotlib.pyplot as plt
import matplotlib
import scipy.linalg as la
from collections import Counter, defaultdict
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 8})
import os
import pandas as pd
import numpy as np
import math

IDs = ["1005_143936"]
species = 10000
rows = 1
columns = 3
dir = "data"

gammas = {"1005_143936": np.ones(10)/la.norm(np.ones(10), ord=0.5),
        "1005_145930": np.ones(10)/la.norm(np.ones(10), ord=0.9)
}

p_norms = {"1005_143936": 0.5,
        "1005_145930": 0.9
}

def plane(X, Y, P_NORM):
    Z = np.empty(np.shape(X.flatten()))

    for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):

        if ((1**P_NORM) - x**P_NORM - y**P_NORM) < 0:
            Z[i] = np.nan
        else:
            Z[i] = ((1**P_NORM) - x**P_NORM - y**P_NORM) ** (1/P_NORM)

    return np.reshape(Z, np.shape(X))


if __name__ == "__main__":

   
    for file_ID in IDs:
        df_strategies = pd.read_csv(f"{file_ID}_strategies.csv")
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv(f"{file_ID}_results.csv", index_col="time", header=0)

        fig = plt.figure()
        num_subplots = rows*columns
        timestep = int(np.max(df_abundances.index)/(num_subplots*100))*100

        for t in np.arange(1000,  timestep*(num_subplots), timestep):
            loc = int(t/timestep)+1  
            ax = fig.add_subplot(rows, columns, loc, projection='3d')
            # ax = fig.add_subplot(2, 2, loc, projection='3d')
            
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
        plt.savefig(f"gammaidentical_eta{file_ID}_Kmax10000_P{p_norms[file_ID]}_{rows}x{columns}.png", dpi=300)
        # plt.show()
        plt.clf()
            

    # this_works = [bool(abundance) for abundance in df_abundances.loc[:, "species" + str(ID)]]
    
