import os
from MA_nonspeciating_abundances import *

# Parameter settings
resources = 20
species = 500
modelruns = 100
PNORMS = [0.9, 1, 1.1]
timesteps = 10000

# Ran once with exponential initialized vectors
# Ran once with standard gaussian initialized vectors
# Ran once with strictly positive gaussian initialized vectors. Used mean 0.5, standarddeviation 0.5 and set all values <0 to 0

if __name__ == "__main__":
    folder = "figD_skewnessovertime_nonspeciating_exp"
    os.mkdir(folder)

    
    for P in PNORMS:
        seed_starter = 123456
        os.mkdir(folder+f"/P{P}")
        

        GAMMA = np.ones(resources) / la.norm(np.ones(resources), ord=P)

        for _ in range(modelruns):
            one_run = ecosystem_nonspeciating(GAMMA=GAMMA,
                                            D_DIMENSION=resources,
                                            P_NORM=P,
                                            K_SPECIES_MAX=species,
                                            DT_TIMESCALE = 0.1,
                                            SEED = seed_starter,
                                            save_every=1000,
                                            result_folder=folder+f"/P{P}")
            one_run.update_system(timesteps)
            seed_starter += 1
