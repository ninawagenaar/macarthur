from MA_speciating import *


# add new folder
# os.mkdir('test')



if __name__ == "__main__":
    folder = "figA_3Dsystem"
    os.mkdir(folder)

    with open(folder+"/PARAMETER_SETTINGS.csv", 'w', newline='') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',')
        testwriter.writerow(["ID", "GAMMA", "D_DIMENSION", "P_NORM", "NOISE", "MEAN", "SIGMA", "K_SPECIES_MAX", "ABUNDANCE_SPAWN", "ABUNDANCE_DEATH", "DEATH_RATE", "ALPHA", "BETA", "DT_TIMESCALE", "MEAN_INTERARRIVAL_TIME", "SEED", "WITH_RUNOUT", "RUNOUT_SCALING", "MONOD", "MONOD_HALF_VELOCITY", "MONOD_MAX_GROWTH", "save_at"])

    for Pnorm in [1, 2, 3]:
        os.mkdir(folder+f"/P{Pnorm}")
