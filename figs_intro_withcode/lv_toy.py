from asyncio.proactor_events import _ProactorReadPipeTransport
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["mathtext.default"] = 'regular' #enable \mathcal{S}
matplotlib.rcParams.update({'font.size': 16})

# predator
a = 3
b = 1

# prey
c = 6
d = 1



dts = [0.001]

fig, ax = plt.subplots(len(dts))


tau = 6

for i, dt in enumerate(dts):
    predator = 5
    predator_plot = [predator]
    prey = 4
    prey_plot = [prey]
    t = 0
    time = [t]

    while t < tau:
        d_predator = (-a*predator + b*predator*prey)*dt
        d_prey = (c*prey - d*predator*prey)*dt
        predator += d_predator
        prey += d_prey
        if prey <= 0:
            prey=0
        if predator <= 0:
            predator=0

        predator_plot.append(predator)
        prey_plot.append(prey)
        t += dt
        time.append(t)
    
    ax.plot(time, predator_plot, label="predator", ls="dotted", c="black")
    ax.plot(time, prey_plot, label="prey", ls="dashed", c="black")
    # ax.set_title("A predator-prey LV system")
    
# plt.legend()
plt.xlabel("$t$")
plt.ylabel("$x_i$")
plt.tight_layout()
plt.savefig("LV_intro.png")
plt.show()