from cProfile import label
import numpy as np
import numpy.linalg as la
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import scipy
from scipy import spatial
matplotlib.rcParams.update({'font.size': 12})


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
    X = np.linspace(-1, 1, 10000)
    Y1, Y2 = circle(X, 0.5)
    plt.plot(X, Y1, c="red", label="$p$ = 0.5")
    plt.plot(X, Y2, c="red")
    Y1, Y2 = circle(X, 1)
    plt.plot(X, Y1, c="blue", label="$p$ = 1")
    plt.plot(X, Y2, c="blue")
    Y1, Y2 = circle(X, 1.5)
    plt.plot(X, Y1, c="orange", label="$p$ = 1.5")
    plt.plot(X, Y2, c="orange")
    Y1, Y2 = circle(X, 2)
    plt.plot(X, Y1, c="purple", label="$p$ = 2")
    plt.plot(X, Y2, c="purple")
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    # plt.legend()
    if show_figures: plt.show()
    plt.clf()

    """Figure to show the effect of varying the norms
    per dimension on the unit circle"""
    X = np.linspace(-1, 1, 10000)
    Y1, Y2 = circle_normvariation(X, 1, 2)
    plt.plot(X, Y1, c="red", label="$x$ in $L_1$, $y$ in $L_2$")
    plt.plot(X, Y2, c="red")
    Y1, Y2 = circle_normvariation(X, 2, 1)
    plt.plot(X, Y1, c="blue", label="$x$ in $L_2$, $y$ in $L_1$")
    plt.plot(X, Y2, c="blue")
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    if save_figures: plt.savefig("normvariation_L1L2_nounitcircles.png")
    if show_figures: plt.show()
    plt.clf()
    
    """Figure to show a dramatic effect of normvariation"""
    X = np.linspace(-1, 1, 10000)
    Y1, Y2 = circle_normvariation(X, 0.01, 5)
    plt.plot(X, Y1, c="red", label="$x$ in $L_{0.01}$, $y$ in $L_5$")
    plt.plot(X, Y2, c="red")
    Y1, Y2 = circle_normvariation(X, 2, 1)
    plt.plot(X, Y1, c="blue", label="$x$ in $L_2$, $y$ in $L_1$")
    plt.plot(X, Y2, c="blue")
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    if show_figures: plt.show()
    plt.clf()
    
    """Figure to show the effect of normvariation compared
    to no normvariation"""
    X = np.linspace(-1, 1, 10000)
    Y1, Y2 = circle(X, 2)
    plt.plot(X, Y1, c="red", label="$p$ = 2")
    plt.plot(X, Y2, c="red")
    Y1, Y2 = circle(X, 0.5)
    plt.plot(X, Y1, c="orange", label="$p$ = 0.5")
    plt.plot(X, Y2, c="orange")
    Y1, Y2 = circle_normvariation(X, 2, 0.5)
    plt.plot(X, Y1, c="blue", label="$x$ in $L_2$, $y$ in $L_{0.5}$")
    plt.plot(X, Y2, c="blue")
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    if show_figures: plt.show()
    plt.clf()
    
    """Figure to show the effect of suble normvariation
    compared to no normvariation"""
    X = np.linspace(-1, 1, 10000)
    Y1, Y2 = circle(X, 2)
    plt.plot(X, Y1, c="purple", ls="dotted", label="$p$ = 2")
    plt.plot(X, Y2, c="purple", ls="dotted")
    Y1, Y2 = circle(X, 1)
    plt.plot(X, Y1, c="orange", ls="dashed", label="$p$ = 1")
    plt.plot(X, Y2, c="orange", ls="dashed")
    Y1, Y2 = circle_normvariation(X, 2, 1)
    plt.plot(X, Y1, c="blue", label="$x$ in $L_2$, $y$ in $L_1$")
    plt.plot(X, Y2, c="blue")
    Y1, Y2 = circle_normvariation(X, 1, 2)
    plt.plot(X, Y1, c="red", label="$x$ in $L_1$, $y$ in $L_2$")
    plt.plot(X, Y2, c="red")
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    if show_figures: plt.show()
    if save_figures: plt.savefig("normvariation_L1L2_withunitcircles.png")
    plt.clf()


    X = np.linspace(0, 1, 10000)
    Y1, Y2 = circle(X, 2)
    plt.plot(X, Y1, c="purple", label="Both in $L_2$")
    Y1, Y2 = circle(X, 1)
    plt.plot(X, Y1, c="blue", label="Both in $L_1$")
    # plt.plot(X, Y2, c="orange", ls="dashed")
    Y1, Y2 = circle(X, 0.5)
    plt.plot(X, Y1, c="orange", label="Both in $L_{0.5}$")
    # plt.plot(X, Y2, c="blue")
    Y1, Y2 = circle_normvariation(X, 0.5, 2)
    plt.plot(X, Y1, c="red", label="$x$ in $L_{0.5}$, $y$ in $L_2$")
    # plt.plot(X, Y2, c="red")
    plt.xlim([-0.1,1.1])
    plt.ylim([-0.1,1.1])
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.legend()
    if save_figures: plt.savefig("normvariation_presentationgroupmeeting21feb.png")
    if show_figures: plt.show()
    plt.clf()

        
    """Figure to show the effect of p in the Lp norm
    on the 2D unit circle. """
    X = np.linspace(0, 1, 10000)
    Y1, Y2 = circle(X, 0.5)
    plt.plot(X, Y1, c="red", label="$L^{0.5}$\nConvex")
    # plt.plot(X, Y2, c="red")
    Y1, Y2 = circle(X, 1)
    plt.plot(X, Y1, c="blue", label="$L^1$\nLinear")
    # plt.plot(X, Y2, c="blue")
    Y1, Y2 = circle(X, 1.5)
    # plt.plot(X, Y1, c="orange", label="$p$ = 1.5")
    # plt.plot(X, Y2, c="orange")
    Y1, Y2 = circle(X, 2)
    plt.plot(X, Y1, c="purple", label="$L^2$\nConcave")
    # plt.plot(X, Y2, c="purple")
    plt.xlim([-0.1,1.1])
    plt.ylim([-0.1,1.1])
    ax = plt.gca()
    ax.legend(loc=(0.8, 0.6))
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()

    if show_figures: plt.show()
    plt.clf()
