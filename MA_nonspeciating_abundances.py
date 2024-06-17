import numpy as np
import csv
from datetime import datetime
import numpy.linalg as la

class ecosystem_nonspeciating:

    def __init__(self, 
                GAMMA = None,
                D_DIMENSION = 5, 
                P_NORM = 1, 
                K_SPECIES_MAX = 100,
                ABUNDANCE_SPAWN = 0.01,
                ABUNDANCE_DEATH = 0.001, #Abundance below threshold --> species extinct.
                DEATH_RATE = 0.1,
                ALPHA = 0.05,
                BETA = 0.01,
                DT_TIMESCALE = 0.001,
                SEED = None,
                MONOD = False, 
                MONOD_HALF_VELOCITY = None, 
                MONOD_ALPHAMAX = None,
                MONOD_BETAMAX = None,
                save_every = 10,
                result_folder = "results"
                ):

        self.GAMMA = GAMMA
        self.D_DIMENSION = D_DIMENSION
        self.P_NORM = P_NORM
        self.K_SPECIES_MAX = K_SPECIES_MAX
        self.ABUNDANCE_SPAWN = ABUNDANCE_SPAWN
        self.ABUNDANCE_DEATH = ABUNDANCE_DEATH
        self.DEATH_RATE = DEATH_RATE
        self.ALPHA = ALPHA
        self.BETA = BETA
        self.DT_TIMESCALE = DT_TIMESCALE
        self.SEED = SEED
        self.MONOD = MONOD
        self.MONOD_HALF_VELOCITY = MONOD_HALF_VELOCITY
        self.MONOD_ALPHAMAX = MONOD_ALPHAMAX
        self.MONOD_BETAMAX = MONOD_BETAMAX
        self.save_every = save_every
        self.result_folder = result_folder
       
        self.time = 0
        self.RNG = np.random.default_rng(seed=self.SEED)
        self.strategies = self.RNG.exponential(size=(K_SPECIES_MAX, D_DIMENSION))
        # self.strategies = self.RNG.uniform(size=(K_SPECIES_MAX, D_DIMENSION))
        for i, strat in enumerate(self.strategies):
            self.strategies[i] = strat/la.norm(strat, ord=P_NORM) #vector containing the strategy vectors
        self.abundances = np.ones(K_SPECIES_MAX)  * ABUNDANCE_SPAWN
        self.resources = np.ones(D_DIMENSION)  #vector containing resource abundances, maybe this is too much for initialization
        self.interarrival_times = np.zeros(K_SPECIES_MAX)
        self.alive = np.ones(K_SPECIES_MAX) #1 if species at ID is alive, 0 if it's not.
        self.start = datetime.now().strftime("%d%m_%H%M%S")
        self.results_csv = result_folder+"/{}_results_nonspeciating.csv".format(self.start)

        if GAMMA is None:
            GAMMA = self.RNG.exponential(size=D_DIMENSION)
            self.GAMMA = GAMMA/la.norm(GAMMA, ord=P_NORM)
        
        if len(GAMMA) != D_DIMENSION:
            raise ValueError(f"GAMMA needs to be of length {D_DIMENSION}.")

        if MONOD:
            self.ALPHA = None
            self.BETA = None
        
        '''write header for csv result file'''
        with open(self.results_csv, 'a', newline='') as csvfile:
            testwriter = csv.writer(csvfile, delimiter=',')
            testwriter.writerow(["time"] + ["resource"+str(i) for i in range(self.D_DIMENSION)]  + ["species"+str(j) for j in range(self.K_SPECIES_MAX)])

        '''initialize counters for efficient storage of results'''
        self.STORAGE_SIZE = 1000
        self.STORAGE_COUNTER = 0
        self.RESULTS = np.ones((self.STORAGE_SIZE, 1+self.D_DIMENSION+self.K_SPECIES_MAX))

        self.RESULTS[self.STORAGE_COUNTER, 0] = 0
        self.RESULTS[self.STORAGE_COUNTER, 1:self.D_DIMENSION+1] = self.resources
        self.RESULTS[self.STORAGE_COUNTER, self.D_DIMENSION+1:1+self.D_DIMENSION+self.K_SPECIES_MAX] = self.abundances

        self.STORAGE_COUNTER += 1

        with open(self.result_folder+"/PARAMETER_SETTINGS.csv", 'a', newline='') as csvfile:
                testwriter = csv.writer(csvfile, delimiter=',')
                testwriter.writerow([self.start, self.GAMMA, self.D_DIMENSION, self.P_NORM, self.K_SPECIES_MAX, self.ABUNDANCE_SPAWN, self.ABUNDANCE_DEATH, self.DEATH_RATE, self.ALPHA, self.BETA, self.DT_TIMESCALE, self.SEED, self.MONOD, self.MONOD_HALF_VELOCITY, self.MONOD_ALPHAMAX, self.MONOD_BETAMAX, self.save_every])
    
    def update_system(self, timesteps):
        '''Integrates system in between speciation events'''

        while self.time < timesteps:
            
            '''Empty storage array if full'''
            if self.STORAGE_COUNTER == self.STORAGE_SIZE:
                with open(self.results_csv, 'a', newline='') as csvfile:
                    testwriter = csv.writer(csvfile, delimiter=',')
                    testwriter.writerows(self.RESULTS)
                    self.STORAGE_COUNTER = 0

            '''update system'''
            self.resources += (self.GAMMA - self.BETA * np.dot(np.array(self.abundances), np.array(self.strategies))) * self.DT_TIMESCALE
            self.abundances += (self.ALPHA * (np.dot(np.array(self.strategies), np.array(self.resources).T)) - self.DEATH_RATE * np.ones(len(self.strategies))) * np.array(self.abundances) * self.DT_TIMESCALE
            self.time += self.DT_TIMESCALE

            '''set resources and abundances to 0 if needed 
            must be done using event in solve_ivp'''
            for i, resource in enumerate(self.resources):
                if resource <= 0:
                    self.resources[i] = 0
            
            for i, abundance in enumerate(self.abundances):
                if abundance <= self.ABUNDANCE_DEATH:
                    self.abundances[i] = 0
                    self.alive[i] = 0

            '''save results every indicated timestep'''
            if round(self.time, int(round(np.log10(1/self.DT_TIMESCALE),0))) % self.save_every == 0:
                self.RESULTS[self.STORAGE_COUNTER, 0] = round(self.time,0)
                self.RESULTS[self.STORAGE_COUNTER, 1:self.D_DIMENSION+1] = self.resources
                self.RESULTS[self.STORAGE_COUNTER, self.D_DIMENSION+1:1+self.D_DIMENSION+self.K_SPECIES_MAX] = self.abundances                 
                self.STORAGE_COUNTER += 1


        '''ensure that all results are included in the csv file'''
        with open(self.results_csv, 'a', newline='') as csvfile:
            testwriter = csv.writer(csvfile, delimiter=',')
            testwriter.writerows(self.RESULTS[:self.STORAGE_COUNTER, :])
            self.STORAGE_COUNTER = 0


        '''write strategies to file'''
        strategies_csv = self.result_folder+"/{}_strategies_nonspeciating.csv".format(self.start)
        with open(strategies_csv, 'a', newline='') as csvfile:
            testwriter = csv.writer(csvfile, delimiter=',')
            testwriter.writerow(["ID"] + ["strat_res"+str(i) for i in range(self.D_DIMENSION)] + ["alive_at_end"])
            for ID, strategy in enumerate(self.strategies):
                testwriter.writerow([ID] + [strat for strat in strategy] + [bool(self.abundances[ID])])

    
if __name__ == "__main__":
    print("Hello Ecosystem!")
