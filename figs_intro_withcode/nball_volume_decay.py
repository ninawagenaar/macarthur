import numpy as np
import numpy.linalg as la
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import scipy
matplotlib.rcParams.update({'font.size': 12})


def volume_ball(D_DIMENSION, P_NORM, RADIUS=1):
    """Returns the volume of the D_DIMENSIONAL n-ball in Lp"""
    return (2*scipy.special.gamma(1/P_NORM + 1))**D_DIMENSION / scipy.special.gamma(D_DIMENSION/P_NORM + 1) * RADIUS**D_DIMENSION

show_figures = False

if __name__ == "__main__":

    """Figure showing the effect of the normalization
    on the decay of the volume of the n-ball when dimensions increase"""
    DIM_LIST = np.arange(2, 25, 1, dtype=int)
    VOL_L05 = np.empty(len(DIM_LIST))
    VOL_L1 = np.empty(len(DIM_LIST))
    VOL_L15 = np.empty(len(DIM_LIST))
    VOL_L2 = np.empty(len(DIM_LIST))

    for i, DIMENSION in enumerate(DIM_LIST):
        VOL_L05[i] = volume_ball(DIMENSION, 0.5)
        VOL_L1[i] = volume_ball(DIMENSION, 1)
        VOL_L15[i] = volume_ball(DIMENSION, 1.5)
        VOL_L2[i] = volume_ball(DIMENSION, 2)

    plt.plot(DIM_LIST, VOL_L05, label="$L_{0.5}$, R=1", c="red")
    plt.plot(DIM_LIST, VOL_L1, label="$L_1$, R=1", c="blue")
    plt.plot(DIM_LIST, VOL_L15, label="$L_{1.5}$, R=1", c="orange")
    plt.plot(DIM_LIST, VOL_L2, label="$L_2$, R=1", c="purple")
    plt.legend()
    plt.xlabel("Dimensions")
    plt.ylabel("Volume")
    plt.tight_layout()
    if show_figures: plt.show()
    plt.clf()

    plt.semilogy(DIM_LIST, VOL_L05, label="$L_{0.5}$, R=1", c="red")
    plt.semilogy(DIM_LIST, VOL_L1, label="$L_1$, R=1", c="blue")
    plt.semilogy(DIM_LIST, VOL_L15, label="$L_{1.5}$, R=1", c="orange")
    plt.semilogy(DIM_LIST, VOL_L2, label="$L_2$, R=1", c="purple")
    plt.legend()
    plt.xlabel("Dimensions")
    plt.ylabel("Volume")
    plt.tight_layout()
    if show_figures: plt.show()
    plt.clf()