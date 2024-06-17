from email import header
import pickle
import os
import numpy as np
import pandas as pd
from collections import Counter
from collections import defaultdict

# Parameter settings
resources = 10
species = 2000
modelruns = 100
PNORMS = [0.5, 1, 2]
SD = 0.01
methods = ["AVG_DIST_TO_GEN", "AVG_DIFF_MAX_MIN", "AVG_DIST_TO_GAMMA", "AVG_SKEWNESS"]


# folder = "figE_death0.01"

'''
Make files for plotting the skewness evolution over time for a nonspeciating model
Results are combined into acsv containing 6 columns with each the total number of skewnesses of living
species at that specific timepoint in each simulation.
'''

if __name__ == "__main__":

    dict_avg_results = defaultdict(defaultdict)
    timesteps = 300

    for P in PNORMS:
        dir = f"P{P}SD{SD}"
        file_IDs = []

        for filename in os.listdir(dir):
            fileID = filename[:11]
            file_IDs.append(fileID)
            
        file_IDs.sort()
        file_IDs_unique = list(Counter(file_IDs).keys())
        
        df_avg_results = pd.DataFrame(data=np.zeros((timesteps,5)), index=np.arange(timesteps), columns=["time"] + methods)

        for fileID in file_IDs_unique:
            df_results = pd.read_csv(f"{dir}/{fileID}_results.csv")
            
            for col in methods:
                df_avg_results[col] += df_results[col] / len(file_IDs_unique)

            for col in methods:
                dict_avg_results[col][P] = df_avg_results[col]
                dict_avg_results[col]["time"] = df_results["time"][:timesteps]

    with open(f'figE_data_weighted.pkl', 'wb') as file:
        pickle.dump(dict_avg_results, file)

    file.close()