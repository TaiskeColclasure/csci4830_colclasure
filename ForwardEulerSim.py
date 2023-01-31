import matplotlib.pyplot as plt
import numpy as  np

#initialize global variables
N = 1000
I = 1
S = N - I
R=0
t = 0
timeCap = 1
gamma = .5
betta = 1.5

#Conntainers
sBucket = [S]
iBucket = [I]
rBucket = [R]
t = 0

def calcForwardStep(_t):
    incidents = (betta * sBucket * I) / N
    recoveries = gamma * I
    print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    return _S, _I, _R

while t < timeCap:
    sDot, iDot, rDot = calcForwardStep(t)
    i+=1

