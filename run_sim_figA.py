import os
from MA_speciating_abundances import *

# Parameter settings
resources = 3
species = 500
PNORMS =  [0.9, 1, 1.5, 2]
timesteps = 10000
seed_starter = 135

if __name__ == "__main__":
    folder = "figA_3Dsystem"
    os.mkdir(folder)

    with open(folder+"/PARAMETER_SETTINGS.csv", 'w', newline='') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',')
        testwriter.writerow(["ID", "GAMMA", "D_DIMENSION", "P_NORM", "NOISE", "MEAN", "SIGMA", "K_SPECIES_MAX", "ABUNDANCE_SPAWN", "ABUNDANCE_DEATH", "DEATH_RATE", "ALPHA", "BETA", "DT_TIMESCALE", "MEAN_INTERARRIVAL_TIME", "SEED", "WITH_RUNOUT", "RUNOUT_SCALING", "MONOD", "MONOD_HALF_VELOCITY", "MONOD_ALPHAMAX", "MONOD_BETAMAX", "save_at"])

    for P in [0.9, 1, 1.5, 2]:
        os.mkdir(folder+f"/P{P}")

        one_run = ecosystem(GAMMA="random",
                            D_DIMENSION=resources,
                            P_NORM=P,
                            K_SPECIES_MAX=species,
                            DT_TIMESCALE = 0.1,
                            SEED = seed_starter,
                            WITH_RUNOUT=True,
                            save_every=1,
                            result_folder=folder)
        one_run.run_sim()
        seed_starter += 1