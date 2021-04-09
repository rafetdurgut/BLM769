# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:30:08 2021

@author: Win7
"""
import numpy as np

class Operators:
    def __init__(self, op_name="insert"):
        self.op_name = op_name
        
    def get_neighbor(self, solution):
        if self.op_name == "insert":
            r1=np.random.randint(0,len(solution))
            r2=np.random.randint(0,len(solution))
            while(r1==r2):
                r2=np.random.randint(0,len(solution))
                
            if r1>r2: 
                solution = np.hstack((solution[0:r2],solution[r1],solution[r2:r1],solution[(r1+1):]))
            else:
                solution = np.hstack((solution[0:r1],solution[(r1+1):r2],solution[r1],solution[r2:]))
            return solution
        if self.op_name == "swap":
            r1=np.random.randint(0,len(solution))
            r2=np.random.randint(0,len(solution))
            while(r1==r2):
                r2=np.random.randint(0,len(solution))
            temp = solution[r1]
            solution[r1] = solution[r2]
            solution[r2] = temp
        return solution
            
        if self.op_name == "inverse":
            r1=np.random.randint(0,len(solution))
            r2=np.random.randint(0,len(solution))
            while(r1==r2):
                r2=np.random.randint(0,len(solution))
            
            temp = solution[min(r1,r2):max(r1,r2)]
            solution[min(r1,r2):max(r1,r2)] =np.flip(temp,0)
        return solution