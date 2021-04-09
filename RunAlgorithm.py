from Problem import ZeroOneKnapsack
from Operators import Operators
from SA import SimulatedAnnealing

problem = ZeroOneKnapsack('data/01KP','f1_l-d_kp_10_269')
operator = Operators('insert')

SA = SimulatedAnnealing(problem, operator,max_iter=1000,cooling_schedule='log')
SA.run()

#Visualize 
from matplotlib import pyplot as plt
plt.plot(SA.convergence,'r')
plt.plot(SA.objHistory,'b')
