#The idea is that this file will generate a figure that displays the relation between the ball and the polytop.

import numpy as np
import scipy.linalg as la

if __name__ == "__main__":
    print(np.ones(81) / la.norm(np.ones(81), ord=4))
    print(1/8.1113)