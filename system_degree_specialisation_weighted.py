import os
from pickle import FALSE
import time
from MA_speciating_degree_specialisation_weighted import *

# Parameter settings
resources = 10
species = 2000
modelruns = 100
PNORMS = [0.5, 1, 2]
noises = [0.01, 0.1]


if __name__ == "__main__":
    folder = "new_results_HERE"
    # os.mkdir(folder)

    for SD in noises:
        for P in PNORMS:
            dead = 0
            seed_starter = 12345678
            os.mkdir(folder+f"/P{P}SD{SD}")

            with open(folder+f"/P{P}SD{SD}/PARAMETER_SETTINGS.csv", 'w', newline='') as csvfile:
                testwriter = csv.writer(csvfile, delimiter=',')
                testwriter.writerow(["ID", "GAMMA", "D_DIMENSION", "P_NORM", "NOISE", "MEAN", "SIGMA", "K_SPECIES_MAX", "ABUNDANCE_SPAWN", "ABUNDANCE_DEATH", "DEATH_RATE", "ALPHA", "BETA", "DT_TIMESCALE", "MEAN_INTERARRIVAL_TIME", "SEED", "WITH_RUNOUT", "RUNOUT_SCALING", "MONOD", "MONOD_HALF_VELOCITY", "MONOD_ALPHAMAX", "MONOD_BETAMAX", "save_at"])

            GAMMA = np.ones(resources) / la.norm(np.ones(resources), ord=P)
            # GAMMA = None

            for _ in range(modelruns):
                one_run = ecosystem(GAMMA=GAMMA,
                                                D_DIMENSION=resources,
                                                P_NORM=P,
                                                SIGMA=SD,
                                                DEATH_RATE = 0.01,
                                                K_SPECIES_MAX=species,
                                                DT_TIMESCALE = 1,
                                                MEAN_INTERARRIVAL_TIME=15,
                                                WITH_RUNOUT=True,
                                                RUNOUT_SCALING=300,
                                                SEED = seed_starter,
                                                save_every=100,
                                                result_folder=folder+f"/P{P}SD{SD}")
                try:
                    one_run.run_sim()
                except:
                    time.sleep(1)
                    dead += 1
                    pass

                seed_starter += 1

            print(dead, " systems died for L", P, "SD", SD)
