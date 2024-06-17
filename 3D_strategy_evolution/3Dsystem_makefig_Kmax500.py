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
species = 500
rows = 1
columns = 3
# ['0205_203057', '0205_203123', '0205_203150', '0205_203220', '0205_203244', '0205_203314', '0205_203349']

gammas = {
"0205_203057": [0.21671153, 0.07068552, 0.62529199],
"0205_203123":  [0.34835188, 0.49686732, 0.15478079],
"0205_203150":  [0.35356888, 0.56050348, 0.08592764],
"0205_203220":  [0.22235491, 0.06018481, 0.91857579],
"0205_203244":  [0.62423473, 0.52583956, 0.25065272],
"0205_203314":  [0.38692511, 0.27533206, 0.88004615],
"0205_203349":  [0.86835016, 0.03263896, 0.49487644]
}

p_norms = {
"0205_203057": 0.9,
"0205_203123": 1,
"0205_203150": 1,
"0205_203220": 1.5,
"0205_203244": 1.5,
"0205_203314": 2,
"0205_203349": 2
}



def plane(X, Y, P_NORM):
    Z = np.empty(np.shape(X.flatten()))

    for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):

        if ((1**P_NORM) - x**P_NORM - y**P_NORM) < 0:
            Z[i] = nan
        else:
            Z[i] = ((1**P_NORM) - x**P_NORM - y**P_NORM) ** (1/P_NORM)

    return np.reshape(Z, np.shape(X))

if __name__ == "__main__":
   
    for file_ID in p_norms.keys():

        df_strategies = pd.read_csv("{0}/{1}_strategies.csv".format(dir, file_ID))
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv("{0}/{1}_results.csv".format(dir, file_ID), index_col="time", header=0)
        fig = plt.figure()
        plt.tight_layout()
        num_subplots = rows*columns
        timestep = int(np.max(df_abundances.index)/(num_subplots*100))*100


        for t in np.arange(timestep,  timestep*(num_subplots+1), timestep):
            loc = int(t/timestep) #+1  
            ax = fig.add_subplot(rows, columns, loc, projection='3d')
            ax.zorder
            ax.scatter(gammas[file_ID][0], gammas[file_ID][1], gammas[file_ID][2] , marker="*", zorder=1000, c="black", s=8)
            (x, y) = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
            z = plane(x, y, p_norms[file_ID])
            ax.plot_surface(x, y, z, color="lightgray", alpha=0.2, zorder=10000)
 
            for ID in range(species):
                if bool(df_abundances.loc[t, "species" + str(ID)]) and not math.isnan(df_abundances.loc[t, "species" + str(ID)]):
                    alive = np.array(df_strategies.loc[ID, :].array)
                    ax.scatter(alive[0], alive[1], alive[2], c="darkgray", zorder=0, alpha=1, s=8)
                    ax.zorder
                 
            ax.set_xlim([0,1])
            ax.set_ylim([0,1])
            ax.set_zlim([0,1])
            ax.invert_yaxis()
            ax.set(xticklabels=[],
                yticklabels=[],
                zticklabels=[])
            ax.set_title(f"$t$={t}")

            # ax.title(t)
        plt.savefig(f"gammarandom_etaY_Kmax500_P{p_norms[file_ID]}_{rows}x{columns}.png", dpi=300)
        # plt.show()
        plt.clf()
            

    # this_works = [bool(abundance) for abundance in df_abundances.loc[:, "species" + str(ID)]]