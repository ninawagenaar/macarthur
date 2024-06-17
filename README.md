# macarthur
These scripts and notebooks are used to study the evolutionary trajectories in MacArthur resource-consumer systems.

Notebooks were used as a testing environment and not used for final simulations.



# PARAMETERS AND TERMINOLOGY
P_NORM          value of p for finding Lp norm \
K_SPECIES_MAX   maximum number of species at start simulation (in nonspeciating)
                number of speciation events (in speciating) \
D_DIMENSION     number of resources in system \
GAMMA           vector with resource influx rates \
NOISE           distribution of noise, constant "normal" \
MEAN            mean of evolutionary noise, constant at 0 \
SIGMA           standard deviation of noise \
ABUNDANCE_SPAWN abundance of newly spawned species, constant 0.01 \
ABUNDANCE_DEATH abundance below which species is considered extinct, constant 0.001 \
DEATH_RATE      species death rate \
ALPHA           rate of reproduction, constant 0.005 \
BETA            rate of consumption, constant 0.01 \
DT_TIMESCALE    size of Euler step \
MEAN_INTERARRIVAL_TIME      average time between speciation events \
SEED            seed for random variables \
WITH_RUNOUT     boolean determining if system will continue running after last speciation event \
RUNOUT_SCALING  amount of time the system will continue running after last speciation event \



# FOLDERS
* 3D_strategy_evolution
Contains scripts and figures used for showing the time evolution of systems with 3 resources. This folder contains additional figures corresponding to figures 3.2 and 3.3 in the report.

* figs_intro_withcode
Contains scripts and figures used to support the introduction. This folder contains older versions of the figures.

* figs_presentation
Contains scripts used to make figures to support the final presentation.

* notebooks
Contains jupyter notebooks with the implementation of both nonspeciating and speciating MacArthur systems. These notebooks were used to test the implementation and are not used for any simulations.

* species_degree_specialisation
Contains scripts and figures used for showing the time evolution of the species leven degree of specialisation.  
  * Figures in nonspeciating_uniformdistribution correspond to figure 3.4, there are no additional figures.
  * Figures in nonspeciating_exponentialdistribution correspond to figure 3.5, there are no additional figures.
  * Figures in speciating_delta0.1 correspond to figures 3.6 and 3.7 in the report and contain additional figures with $\eta=0.1$ and $p = 2$.
  * Figures in speciating_delta0.01 correspond to figures 3.8 and 3.9 in the report and contain additional figures with $p=0.9$, $p=1$, $p=1.1$.

* system_degree_specialisation
Contains scripts and figures used for showing the time evolution of the system level degree of specialisation.
  * Figures in not_weighted correspond to figures 3.10, 3.11, 3.12, and 3.13 in the report. This folder contains many additional figures, both for parameters and method of studying $S$.
  * Figures in weighted correspond to figures 3.14 and 3.15 in the report. This folder contains additional figures for different methods of studying $S$.

# FILES
