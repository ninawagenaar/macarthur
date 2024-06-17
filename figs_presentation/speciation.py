import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from colors import *
matplotlib.rcParams.update({'font.size': 18})


plt.bar([1, 2, 3], [0.3, 0.6, 0.1], align='center', color=colors[1:4])
plt.gca().set_xticks([1, 2, 3])
# plt.plot(bin_centres, values)
plt.xlabel("species")
plt.ylabel("species relative abundance")
plt.tight_layout()
plt.savefig("speciation_probability.png", dpi=300)
plt.show()