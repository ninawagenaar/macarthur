import os
import time
from MA_speciating_abundances import *

# Parameter settings
resources = 10
species = 1000
modelruns = 100
PNORMS = [0.9, 1, 1.1]
# timesteps = 10000


if __name__ == "__main__":
    folder = "figD_skewnessovertime_speciating_exp"
    os.mkdir(folder)

    
    for P in PNORMS:
        dead = 0
        seed_starter = 1234567
        os.mkdir(folder+f"/P{P}")

        with open(folder+f"/P{P}/PARAMETER_SETTINGS.csv", 'w', newline='') as csvfile:
            testwriter = csv.writer(csvfile, delimiter=',')
            testwriter.writerow(["ID", "GAMMA", "D_DIMENSION", "P_NORM", "NOISE", "MEAN", "SIGMA", "K_SPECIES_MAX", "ABUNDANCE_SPAWN", "ABUNDANCE_DEATH", "DEATH_RATE", "ALPHA", "BETA", "DT_TIMESCALE", "MEAN_INTERARRIVAL_TIME", "SEED", "WITH_RUNOUT", "RUNOUT_SCALING", "MONOD", "MONOD_HALF_VELOCITY", "MONOD_ALPHAMAX", "MONOD_BETAMAX", "save_at"])

        GAMMA = np.ones(resources) / la.norm(np.ones(resources), ord=P)

        for _ in range(modelruns):
            one_run = ecosystem(GAMMA=GAMMA,
                                            D_DIMENSION=resources,
                                            P_NORM=P,
                                            K_SPECIES_MAX=species,
                                            DT_TIMESCALE = 0.1,
                                            MEAN_INTERARRIVAL_TIME=10,
                                            WITH_RUNOUT=True,
                                            RUNOUT_SCALING=100,
                                            SEED = seed_starter,
                                            save_every=1000,
                                            result_folder=folder+f"/P{P}")
            try:
                one_run.run_sim()
            except:
                time.sleep(1)
                dead += 1
                pass

            seed_starter += 1

        print(dead, " systems died for L", P)
