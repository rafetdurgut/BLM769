#Kutuphaneleri dahil edelim.
import numpy as np


class ZeroOneKnapsack:
    def __init__(self, folderName, fileName):
        self.fileName = fileName
        self.folderName = folderName
        self.weights = []
        self.profits = []
        self.qualities = []
        self.non_qualities = []
        
        with open(f"{folderName}/{fileName}") as f:
            self.dim, self.capacity = map(int, f.readline().split())
            for i in range(self.dim):
                p_i, w_i = map(float, f.readline().split())
                self.weights.append(w_i)
                self.profits.append(p_i)
                self.qualities.append(p_i/w_i)
                self.non_qualities.append(w_i/p_i)
                
                
    def optimizing_stage(self, solution):
        #Çanta kapasitesi
        cap_val = np.dot(self.weights,solution)
        #Çanta içinde olmayan elemanların kaliteleri
        qualities = np.multiply(self.qualities, solution == 0)
        #Çanta içinde olmayan en kaliteli elemanın indisi
        add_index = np.argmax(np.multiply(qualities, solution==0))
        while cap_val + self.weights[add_index] <= self.capacity:
            solution[add_index] = True
            qualities[add_index] = 0
            cap_val += self.weights[add_index]
            add_index = np.argmax(qualities)
        return solution


    def repair(self, solution):
        cap_val = np.dot(self.weights, solution)
        qualities = np.multiply(self.non_qualities, solution==1)
        #Çanta içinde olan en düşük faydalı elemanın indisi
        while cap_val > self.capacity:
            remove_index = np.argmax(qualities)
            solution[remove_index] = False
            qualities[remove_index] = 0
            cap_val -= self.weights[remove_index]
        return solution            
    
    def objective_function(self, solution):
            cap_val = np.dot(self.weights, solution)
            if cap_val > self.capacity:
                solution = self.repair(solution)
                solution = self.optimizing_stage(solution)
            else:
                solution = self.optimizing_stage(solution)
    
            cap_val = np.dot(self.weights, solution)
            sum_val = np.dot(self.profits, solution)
            return sum_val

class OneMax:
    def __init__(self, dim):
        self.dim = dim
         
        
    def objective_function(self, solution):
        return np.sum(solution)




#Problem sınıfı 
class TSP:
    #Problemin dosyasi
    def __init__(self, folderName, fileName):
        self.fileName = fileName
        self.folderName = folderName
        self.positions = []
        
        #Dosya okuma
        with open(f"{folderName}/{fileName}") as f:
            f.readline()
            f.readline()
            f.readline()
            a,b = f.readline().split(':')
            self.dim = int(b)
            f.readline()
            f.readline()
            for i in range(self.dim):
                line = f.readline().split()
                self.positions.append([int(line[1]), int(line[2])])
                
                
    def objective_function(self, sol):
        total_cost = 0
        for i in range(self.dim-1):
            a = self.positions[ sol[i] ]
            b = self.positions[ sol[i+1] ]
            total_cost += np.round( np.sqrt ( (a[0]-b[0])**2 + (a[1]-b[1])**2 ) )
            
        a = self.positions[ sol[self.dim-1] ]
        b = self.positions[ sol[0] ]
        total_cost += np.round( np.sqrt ( (a[0]-b[0])**2 + (a[1]-b[1])**2 ) )
        return total_cost



