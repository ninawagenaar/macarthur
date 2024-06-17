import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 22})


from degspec_plot_preprocess import *

ylabels = ["$\mathcal{S}_{gen}$", "$\mathcal{S}_{diff}$", "$\mathcal{S}_{\gamma}$", "$\mathcal{S}_{skew}$"]
linestyles = ["solid", "dashed", "dotted"]

if __name__ == "__main__":

    for P in PNORMS:
        # for SD in noises:
            
        with open(f'figE_data_P{P}.pkl', 'rb') as file:
            avg_results = pickle.load(file)
        file.close()
         
        for method, ylabel in zip(methods, ylabels):
            for SD, style in zip(noises, linestyles):
                plt.plot(avg_results[method]["time"], avg_results[method][SD], c="black", label="$\eta$ = " +str(SD), ls=style)

            plt.xlabel("t")
            plt.ylabel(ylabel)
            # plt.legend()
            plt.tight_layout()
            plt.savefig(f"figE_P{P}_method{method}.png")
            # plt.show()
            plt.clf()
