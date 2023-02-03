import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
def g(x):
    expon = -rNot * x
    secndTerm = math.e ** expon
    result = 1- secndTerm
    return result
def f(x):
    return x

def h(x):
    return f(x)-g(x)


rNot = 2
rInf = np.arange(0,1,.01)
gRinfs = np.array(list(map(g, rInf)))
root = fsolve(h, 1)
plt.figure(figsize=(8,8))
plt.title("rInf: {} Insection: {}, {}".format(rNot, root, g(root)))
plt.plot(gRinfs, rInf, color="black")
plt.plot(rInf, rInf, color="red")
plt.scatter(g(root), root, color="blue")
plt.show()
