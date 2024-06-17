import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 22})


from degspec_plot_preprocess import *

ylabels = ["$\mathcal{S}_{gen}$", "$\mathcal{S}_{diff}$", "$\mathcal{S}_{\gamma}$", "$\mathcal{S}_{skew}$"]
ylimits = [[0, 0.8], [0, 0.7], [0, 0.8], [-0.1, 3]]
linestyles = ["solid", "dashed", "dotted"]

if __name__ == "__main__":
        # for SD in noises:
            
    with open(f'figE_data_weighted.pkl', 'rb') as file:
        avg_results = pickle.load(file)
    file.close()
        
    for method, ylabel, ylimit in zip(methods, ylabels, ylimits):
        for P, style in zip(PNORMS, linestyles):
            plt.plot(avg_results[method]["time"], avg_results[method][P], c="black", label="$p$ = " +str(P), ls=style)

        plt.xlabel("t")
        plt.ylabel(ylabel)
        # plt.legend()
        plt.tight_layout()
        plt.ylim(ylimit)
        plt.savefig(f"figE_method{method}_adjustedbiomass.png")
        # plt.show()
        plt.clf()
