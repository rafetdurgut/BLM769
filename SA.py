
import numpy as np

class SimulatedAnnealing:
    def __init__(self, problem, operator, max_iter=100, alpha=1, cooling_schedule='linear',initial_temp = 1000):
        self.problem = problem
        self.operator = operator
        self.max_iter = max_iter
        self.cooling_schedule = cooling_schedule
        self.initial_temp = initial_temp
        self.gbest = []
        self.gbest_val = 0;
        self.alpha = alpha
        self.convergence = []
        self.objHistory = []
        
    def get_temperature(self, t):
        if self.cooling_schedule == 'linear':
            return ((1-(t/self.initial_temp))** 1) * self.initial_temp
        elif self.cooling_schedule == 'poly':
            return ((1-(t/self.initial_temp))** self.alpha) * self.initial_temp
        elif self.cooling_schedule == 'log':
            if(t<3):
                return self.initial_temp
            return self.initial_temp / np.log(t)
        elif self.cooling_schedule == 'exp':
            return ((1-0.05)** t) * self.initial_temp
    
    def run(self):
        self.solution = np.random.permutation(self.problem.dim)
        self.objval = self.problem.objective_function(self.solution)
        
        self.gbest = self.solution.copy()
        self.gbest_val =self.objval
        t=0
        while t < self.max_iter:
            neighbor = self.operator.get_neighbor(self.solution.copy())
            obj = self.problem.objective_function(neighbor)
            delta = obj - self.objval
            
            if(delta < 0):
                self.solution = neighbor
                self.objval = obj
            else:
                
                temperature = self.get_temperature(t)
                acceptance_probability = np.exp(- delta/temperature)
                if(np.random.random() < acceptance_probability):
                    self.solution = neighbor
                    self.objval = obj
            
            if self.objval<self.gbest_val:
                self.gbest_val = self.objval
                self.gbest = self.solution.copy()
                
            self.convergence.append(self.gbest_val)
            self.objHistory.append(self.objval)
            t += 1
                
                
            


        