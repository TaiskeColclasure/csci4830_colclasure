import matplotlib.pyplot as plt
import numpy as np

#initialize global variables
N = 1000
I = 1
S = N - I
R=0
t = 0
timeCap = 50
gamma = .5
betta = 1
deltaT = .5

#Conntainers
sBucket = [S]
iBucket = [I]
rBucket = [R]
tBucket = [0]
t = 0

def displayResults():
    plt.plot(tBucket, sBucket, label = "S taiske")
    plt.plot(tBucket, iBucket, label = "I taiske")
    plt.plot(tBucket, rBucket, label = "R taiske")
    plt.legend()
    plt.title('SIR model with beta: {}  and gamma: {}'.format(betta, gamma))
    plt.savefig('SIR_model_beta-{}_gamma:_{}.jpg'.format(betta, gamma))

def calcForwardStep():
    incidents = (betta * sBucket[-1] * iBucket[-1]) / N
    recoveries = gamma * iBucket[-1] 
    print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    sSot = -incidents
    iDot = incidents - recoveries
    rDot = recoveries
    return -incidents, incidents - recoveries, recoveries

def applyStepChanges(_sDot, _iDot, _rDot):
    sBucket.append(sBucket[-1] + (deltaT * _sDot))
    iBucket.append(iBucket[-1] + (deltaT * _iDot))
    rBucket.append(rBucket[-1] + (deltaT * _rDot))
    tBucket.append(tBucket[-1] + deltaT)
    
#Time loop
while t < timeCap:
    sDot, iDot, rDot = calcForwardStep()
    applyStepChanges(sDot, iDot, rDot)
    t += deltaT

displayResults()
