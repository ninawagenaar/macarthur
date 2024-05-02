import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 22})


from skewness_plot_preprocess import *

bin_width = 0.1

if __name__ == "__main__":

    for P in PNORMS:
        for SD in noises:
            with open(f'skewnessplot_data_P{P}SD{SD}.pkl', 'rb') as file:
                skewness_to_plot = pickle.load(file)
            file.close()

            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')

            for key in skewness_to_plot.keys():
                hist, bin_edges = np.histogram(skewness_to_plot[key], bins=np.arange(np.min(skewness_to_plot[key]), np.max(skewness_to_plot[key]), bin_width), density=True)
                bin_centres = [((bin_edges[i-1] + bin_edges[i])/2) for i in range(1, len(bin_edges))]

                ax.plot(bin_centres, hist/(1/bin_width), zs=key, zdir='y', color="black")
                    
            ax.set_xlabel("$s(\sigma_j)$")
            ax.set_ylabel("$t$")
            ax.set_zlabel("$p(s(\sigma_j))$")
            ax.invert_yaxis()

            plt.savefig(f"figD_probabilities_3D_P{P}SD{SD}_speciating.png")
            # plt.show()
            plt.clf()
            

            linestyles = ['dotted', (0,(2,2)), (0,(3,3)), (0,(4,2)), (0,(5,1)),'solid']
            for key, style in zip(skewness_to_plot.keys(), linestyles):
                hist, bin_edges = np.histogram(skewness_to_plot[key], bins=np.arange(np.min(skewness_to_plot[key]), np.max(skewness_to_plot[key]), bin_width), density=True)
                bin_centres = [((bin_edges[i-1] + bin_edges[i])/2) for i in range(1, len(bin_edges))]

                plt.plot(bin_centres, hist/(1/bin_width), linestyle=style, color="black", label="$t$ = " + str(int(key/1000)))

            # plt.legend()
            plt.xlabel("$s_{skew}(\sigma_j)$")
            plt.ylabel("$p(s_{skew}(\sigma_j))$")
            plt.ylim([0,0.15])
            plt.tight_layout()
            plt.savefig(f"figD_probabilities_2D_P{P}SD{SD}_speciating.png")
            plt.show()

