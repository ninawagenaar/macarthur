from cProfile import label
import numpy as np
import numpy.linalg as la
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import scipy
from scipy import spatial
from colors import *
matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}


# Set to True if saving of figures is desired
save_figures = False

# Set to True if showing of figures is desired
show_figures = False

def circle(X, P_NORM):
    ''' Helper function for creating 2D unit circles
    X is numpy array'''
    Y = ((1**P_NORM) - (abs(X)**P_NORM)) ** (1/P_NORM)
    return Y, -Y


def circle_normvariation(X, P_NORM_X, P_NORM_Y):
    ''' Helper function for creating 2D unit circles with varying norms
    X is numpy array'''
    Y = (1 - (abs(X)**P_NORM_X)) ** (1/P_NORM_Y)
    return Y, -Y


if __name__ == "__main__":

    
    """Figure to show the effect of p in the Lp norm
    on the 2D unit circle. """
    X = np.linspace(0, 1, 10000)
    Y1, _ = circle(X, 0.5)
    plt.plot(X, Y1, c=colors[1], label="$p$<1", linewidth=5.0)
    Y2, _ = circle(X, 1)
    plt.plot(X, Y2, c=colors[2], label="$p$=1", linewidth=5.0)
    Y3, _ = circle(X, 2)
    plt.plot(X, Y3, c=colors[3], label="$p$>1", linewidth=5.0)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    # plt.xlabel("sleep")
    # plt.ylabel("study")
    ax = plt.gca()
    ax.legend(loc=(0.85, 0.65))
    # ax.set(xticklabels=[],
    #             yticklabels=[]
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    plt.savefig("tradeoffs_3_color_largeletter.png")
    # plt.show()
    plt.clf()

    """Figures to show speciation """
    noise = [0.1, 0.4]
    ancestor = np.array([0.5, 0.5])
    new_notnormal = ancestor + noise
    newnormal = new_notnormal / la.norm(new_notnormal, ord=1)
    data = np.stack((ancestor, new_notnormal, newnormal), axis=1)

    # stage 1
    plt.plot(X, Y2, c=colors[2], label="$p= $ linear", linewidth=2.0)
    plt.scatter(ancestor[0], ancestor[1], color=colors[0], zorder=5)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')  
    plt.xlim([-0.05,1.2])
    plt.ylim([-0.05,1.05])
    plt.tight_layout()
    # plt.savefig("speciation_step1.png", dpi=300)
    # plt.show()
    plt.clf()

    # stage 2
    plt.plot(X, Y2, c=colors[2], label="$p= $ linear", linewidth=2.0)
    plt.scatter(new_notnormal[0], new_notnormal[1], color=colors[1], zorder=5)
    plt.plot(data[0, :2], data[1, :2], color=colors[3])
    plt.scatter(ancestor[0], ancestor[1], color=colors[0], zorder=5)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')  
    plt.xlim([-0.05,1.2])
    plt.ylim([-0.05,1.05])
    plt.tight_layout()
    # plt.savefig("speciation_step2.png", dpi=300)
    # plt.show()
    plt.clf()

    # stage 3
    plt.plot(X, Y2, c=colors[2], label="$p= $ linear", linewidth=2.0)
    plt.scatter(ancestor[0], ancestor[1], color=colors[0], zorder=5)
    plt.scatter(new_notnormal[0], new_notnormal[1], color=colors[1], zorder=5)
    plt.scatter(newnormal[0], newnormal[1], color=colors[1], zorder=5)
    plt.plot(data[0, 1:], data[1, 1:], color=colors[3])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')  
    plt.xlim([-0.05,1.2])
    plt.ylim([-0.05,1.05])
    plt.tight_layout()
    # plt.savefig("speciation_step3.png", dpi=300)
    # plt.show()
    plt.clf()

    # stage 4
    plt.plot(X, Y2, c=colors[2], label="$p= $ linear", linewidth=2.0)
    plt.scatter(ancestor[0], ancestor[1], color=colors[0], zorder=5)
    plt.scatter(newnormal[0], newnormal[1], color=colors[0], zorder=5)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')  
    plt.xlim([-0.05,1.2])
    plt.ylim([-0.05,1.05])
    plt.tight_layout()
    # plt.savefig("speciation_step4.png", dpi=300)
    # plt.show()
    plt.clf()