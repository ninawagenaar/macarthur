import matplotlib.pyplot as plt

from skewness_plot_preprocess import *


if __name__ == "__main__":

    for P in PNORMS:
        with open(f'skewnessplot_data_p{P}.pkl', 'rb') as file:
            skewness_to_plot = pickle.load(file)
        file.close()

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for key in skewness_to_plot.keys():
            hist, bin_edges = np.histogram(skewness_to_plot[key], bins=40, density=False)
            bin_centres = [((bin_edges[i-1] + bin_edges[i])/2) for i in range(1, len(bin_edges))]

            ax.plot(bin_centres, hist, zs=key, zdir='y', color="black")
                
        ax.set_xlabel("$s(\sigma_j)$")
        ax.set_ylabel("$t$")
        ax.set_zlabel("$c(s(\sigma_j))$")
        ax.invert_yaxis()

        plt.savefig(f"figD_absolute_3D_P{P}.png")
        plt.show()
        plt.clf()
        

        linestyles = ['dotted', (0,(2,2)), (0,(3,3)), (0,(4,2)), (0,(5,1)),'solid']
        for key, style in zip(skewness_to_plot.keys(), linestyles):
            hist, bin_edges = np.histogram(skewness_to_plot[key], bins=40, density=False)
            bin_centres = [((bin_edges[i-1] + bin_edges[i])/2) for i in range(1, len(bin_edges))]

            plt.plot(bin_centres, hist, linestyle=style, color="black", label="$t$ = " + str(key))

        plt.legend()
        plt.xlabel("$s(\sigma_j)$")
        plt.ylabel("$c(s(\sigma_j))$")
        plt.savefig(f"figD_absolute_2D_P{P}_uni.png")
        plt.show()

