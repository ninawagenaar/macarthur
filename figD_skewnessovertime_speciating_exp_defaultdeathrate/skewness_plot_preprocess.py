import pickle
import os
import numpy as np
import pandas as pd
from collections import Counter
from collections import defaultdict

# Parameter settings
resources = 10
species = 500
modelruns = 100
PNORMS = [0.9, 1, 1.1]
noises = [0.01, 0.1, 1]
timesteps = 10000
# folder = "figD_skewnessovertime_nonspeciating"

'''
Make files for plotting the skewness evolution over time for a nonspeciating model
Results are combined into acsv containing 6 columns with each the total number of skewnesses of living
species at that specific timepoint in each simulation.
'''

if __name__ == "__main__":

    for P in PNORMS:
        for SD in noises:
            dir = f"P{P}SD{SD}"
            file_IDs = []

            for filename in os.listdir(dir):
                fileID = filename[:11]
                file_IDs.append(fileID)
            file_IDs.sort()
            file_IDs_unique = list(Counter(file_IDs).keys())

            timepoints = np.linspace(0, timesteps, 6)
            specie_IDs = np.linspace(0, species-1, species, dtype=int)
            skewness_to_plot = defaultdict(list)

            for fileID in file_IDs_unique:
                df_strategies = pd.read_csv("{0}/{1}_strategies.csv".format(dir, fileID))
                drop_col = ["ID", "ancestor", "alive_at_end"]
                df_strategies.drop(columns=drop_col, inplace=True)
                df_strategies["skewness"] = df_strategies.skew(axis=1)

                df_abundances = pd.read_csv("{0}/{1}_results.csv".format(dir, fileID), index_col="time", header=0)

                for i in timepoints:
                    for ID in specie_IDs:
                        if df_abundances.loc[i, "species" + str(ID)]:
                            skewness_to_plot[i].append(df_strategies.loc[ID, "skewness"])

            with open(f'skewnessplot_data_P{P}SD{SD}.pkl', 'wb') as file:
                pickle.dump(skewness_to_plot, file)

            file.close()