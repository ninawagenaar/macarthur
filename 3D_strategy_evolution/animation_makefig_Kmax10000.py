import matplotlib.animation
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from animation_preprocess_Kmax10000 import *

IDs = ["1005_143936"]

def plane(X, Y, P_NORM):
    Z = np.empty(np.shape(X.flatten()))

    for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):

        if ((1**P_NORM) - x**P_NORM - y**P_NORM) < 0:
            Z[i] = np.nan
        else:
            Z[i] = ((1**P_NORM) - x**P_NORM - y**P_NORM) ** (1/P_NORM)

    return np.reshape(Z, np.shape(X))


def update_graph(num):
    ax.cla()
    data=df[df['time']==num]
    ax.scatter(gammas[fileID][0], gammas[fileID][1], gammas[fileID][2], c="#233c4b", marker="*")
    ax.scatter(data.x, data.y, data.z, c="gray", alpha=0.9)
    ax.plot_surface(x, y, z, color=planecolor, alpha=0.2, shade=False)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([0,1])
    # ax.invert_xaxis()
    ax.invert_yaxis()
    # ax.invert_zaxis()
    title.set_text('3D Test, time={}'.format(num))

if __name__ == "__main__":


    for fileID in IDs:
        
        with open(f'{fileID}_animation_preprocessed.pkl', 'rb') as file:
            df = pickle.load(file)
        file.close()
            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set(xticklabels=[],
                yticklabels=[],
                zticklabels=[])
        title = ax.set_title('3D Test')

        data=df[df['time']==0]
        graph = ax.scatter(data.x, data.y, data.z)
        (x, y) = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
        z = plane(x, y, p_norms[fileID])
        planecolor = colors[p_norms[fileID]]

        ani = matplotlib.animation.FuncAnimation(fig, update_graph, int(np.max(df['time'])), 
                                    interval=250, blit=False)

        ani.save(f"anim_test_{fileID}_plane.mp4", fps=100, dpi=300)
        # plt.show()
