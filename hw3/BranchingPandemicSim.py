import matplotlib.pyplot as plt
import numpy as np
import sys
import math
from scipy.stats import nbinom
from scipy.stats import bernoulli

initialSize = 1
infections = initialSize

gMax = 100
g = 0

k = .1
r0 = 3
mean = r0
variance = mean + (mean ** 2/ k)
p = mean / variance
n = mean ** 2 /(variance - mean)
gamma = .2

infectionBucket = []

trys = 100000
outbreaks = 0
i = 0
while i < trys:
    infections = initialSize
    g=0
    maxOutbreak  = 0
    while (infections < 400 and g < gMax and infections != 0):
        j = 0
        g += 1
        newInfections = nbinom.rvs(n=n, p=p, size=infections)
        recoveries = bernoulli.rvs(gamma, size=infections)
        infections += sum(newInfections)
        infections -= sum(recoveries)
        if infections > maxOutbreak:
            maxOutbreak = infections
    i += 1
    if infections > 1:
        outbreaks += 1
    else:
        infectionBucket.append(maxOutbreak)
    print('Gen:{}, finalSize: {}'.format(i, infections))
print(outbreaks/trys)
plt.hist(infectionBucket, density=True)
plt.show()
