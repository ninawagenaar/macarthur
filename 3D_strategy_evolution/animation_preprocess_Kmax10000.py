import numpy as np
import pandas as pd
from collections import Counter, defaultdict
import math
import scipy.linalg as la
import pickle

IDs = ["1005_143936", "1005_145930"]
species = 10000

dir = None
gammas = {"1005_143936": np.ones(10)/la.norm(np.ones(10), ord=0.5),
        "1005_145930": np.ones(10)/la.norm(np.ones(10), ord=0.9)
}

p_norms = {"1005_143936": 0.5,
        "1005_145930": 0.9
}

colors = {
    0.5: "#ff7d2d", 
    0.9: "#ff7d2d", 
    1: "#fac846", 
    1.1: "#a0c382", 
    2: "#a0c382"
}

if __name__ == "__main__":
    for fileID in IDs:
        df_strategies = pd.read_csv(f"{fileID}_strategies.csv")
        drop_col = ["ID", "ancestor", "alive_at_end"]
        df_strategies.drop(columns=drop_col, inplace=True)

        df_abundances = pd.read_csv(f"{fileID}_results.csv", index_col="time", header=0)
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

        with open(f'{fileID}_animation_preprocessed.pkl', 'wb') as file:
            pickle.dump(df, file)
        file.close()
