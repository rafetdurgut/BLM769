# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:22:14 2021

@author: Win7
"""
from Problem import TSP
from Operators import Operators
import numpy as np
           

class SimulatedAnnealing:
    def __init__(self, problem, operator, max_iter = 1000, random_run=5):
        self.max_iter = max_iter
        self.problem = problem
        self.operator = operator
        self.random_run = random_run
        self.alpha = 2
        self.initial_temp = 1000
        self.gbest = []
        self.gbest_val = 0;
    def is_available(self, pos,  solution):
        if pos in self.problem.houses or pos in solution:
            return False
        return True
    def get_temperature(self,t):
        return self.initial_temp / np.log(t)
        return ((1-(t/self.max_iter))** self.alpha) * self.initial_temp
    
    def run(self):
        self.solutions=[]
        self.objectives = []
        for r in range(self.random_run):
            t = 0
            self.solution = np.random.permutation(self.problem.dim)
            self.obj_val = self.problem.objective_function(self.solution)
            
            self.gbest = self.solution.copy()
            self.gbest_val = self.obj_val
            
            while t < self.max_iter:
                neighbor = self.operator.get_neighbor(self.solution.copy())
                obj = self.problem.objective_function(neighbor)     
                delta = obj - self.obj_val
                temperature = self.get_temperature(t)
                if ( delta < 0 or np.random.random() < np.exp(-delta/temperature) ):
                    self.obj_val = obj
                    self.solution = neighbor
                t += 1
                if(self.obj_val < self.gbest_val):
                    self.gbest_val = self.obj_val
                    self.gbest = self.solution
                
                print(self.gbest_val)
                
            self.solutions.append(self.gbest)
            self.objectives.append(self.gbest_val)

problem = TSP('data/TSP','a280.tsp.txt')
operator = Operators(op_name='inverse')
HC = SimulatedAnnealing(problem,operator,max_iter=100000)   
HC.run() 
for r in range(HC.random_run):
    print(f"{HC.solutions[r]} solution cost: {HC.objectives[r]}")    
    
print(f"Best solution cost: {min(HC.objectives)}")