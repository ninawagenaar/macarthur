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
['0205_203057', '0205_203123', '0205_203150', '0205_203220', '0205_203244', '0205_203314', '0205_203349']

gammas = {
"0205_203057": [0.21671153, 0.07068552, 0.62529199],
"0205_203123":  [0.34835188, 0.49686732, 0.15478079],
"0205_203150":  [0.35356888, 0.56050348, 0.08592764],
"0205_203220":  [0.22235491, 0.06018481, 0.91857579],
"0205_203244":  [0.62423473, 0.52583956, 0.25065272],
"0205_203314":  [0.38692511, 0.27533206, 0.88004615],
"0205_203349":  [0.86835016, 0.03263896, 0.49487644]
}

if __name__ == "__main__":
    file_IDs = [filename[:11] for filename in os.listdir("data")]
    file_IDs.sort()
    file_IDs_unique = list(Counter(file_IDs).keys())

   
    for file_ID in file_IDs_unique:
        df_strategies = pd.read_csv("{0}/{1}_strategies.csv".format(dir, file_ID))
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv("{0}/{1}_results.csv".format(dir, file_ID), index_col="time", header=0)

        fig = plt.figure()
        for t in np.arange(0, 12000, 1000):
            loc = int(t/1000)  
            
            ax = fig.add_subplot(3, 4, loc+1, projection='3d')
            
            for ID in range(500):
                if bool(df_abundances.loc[t, "species" + str(ID)]) and not math.isnan(df_abundances.loc[t, "species" + str(ID)]):
                    alive = np.array(df_strategies.loc[ID, :].array)
                    ax.scatter(alive[0], alive[1], alive[2], c="grey", zorder=0, alpha=0.7, s=2)
                    ax.zorder

            ax.scatter(gammas[file_ID][0], gammas[file_ID][1], gammas[file_ID][2] , marker="*", zorder=1000, c="black")
            ax.zorder
                    
            ax.set_xlabel("$\sigma_1$")
            # ax.set_ylabel("$\sigma_2$")
            # ax.set_zlabel("$\sigma_3$")
            ax.set_xlim([0,1])
            ax.set_ylim([0,1])
            ax.set_zlim([0,1])
            ax.invert_xaxis()
            ax.invert_yaxis()

            # ax.title(t)
        plt.savefig(f"test_{file_ID}.png")
        # plt.show()
        plt.clf()
            

    # this_works = [bool(abundance) for abundance in df_abundances.loc[:, "species" + str(ID)]]