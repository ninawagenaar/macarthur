import time
import os
from MA_speciating_abundances import *

# Parameter settings
resources = 3
species = 1000
seed_starter = 52345327217

if __name__ == "__main__":
    folder = "figA_3Dsystem_uniformgamma"
    os.mkdir(folder)

    with open(folder+"/PARAMETER_SETTINGS.csv", 'w', newline='') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',')
        testwriter.writerow(["ID", "GAMMA", "D_DIMENSION", "P_NORM", "NOISE", "MEAN", "SIGMA", "K_SPECIES_MAX", "ABUNDANCE_SPAWN", "ABUNDANCE_DEATH", "DEATH_RATE", "ALPHA", "BETA", "DT_TIMESCALE", "MEAN_INTERARRIVAL_TIME", "SEED", "WITH_RUNOUT", "RUNOUT_SCALING", "MONOD", "MONOD_HALF_VELOCITY", "MONOD_ALPHAMAX", "MONOD_BETAMAX", "save_at"])

    fails = []
    for P in [0.5, 0.9, 1, 1.1, 2]:
        for SD in [0.01, 0.1, 1]:

            one_run = ecosystem(D_DIMENSION=resources,
                                P_NORM=P,
                                GAMMA = np.ones(resources) / la.norm(np.ones(resources), ord = P),
                                K_SPECIES_MAX=species,
                                DT_TIMESCALE = 0.1,
                                SEED = seed_starter,
                                WITH_RUNOUT=False,
                                save_every=100,
                                SIGMA = SD,
                                result_folder=folder)
            try:
                one_run.run_sim()
            except:
                fails.append((P, SD))
                time.sleep(1)
            seed_starter += 381
    
    print(fails)