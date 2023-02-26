import math
import matplotlib.pyplot as plt
import sys

def f(n):
   return math.log(n) 

data = [
        0.05566091365704323,
        0.017977617450055328,
        0.0075125400118754015,
        0.003548187528024327,
        0.00170771809841469,
        0.0008393164666554709,
        0.00041578119340890396
        ]
data = list(map(f,data))
xAxis = [
        2,
        1,
        .5,
        .25,
        .125,
        .0625,
        .03125
        ]
xAxis = list(map(f, xAxis))
plt.title('Error In Euler Sim vs Delta t (log log)')
plt.xlabel('log(delta t)')
plt.ylabel('log(Error)')
plt.plot(xAxis, data)
plt.xlim(max(xAxis), min(xAxis))
plt.ylim(min(data), max(data))
plt.savefig('brug')
