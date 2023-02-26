import matplotlib.pyplot as plt
import numpy as np
import sys
if(len(sys.argv) != 5):
   print('Usage: python3 ForwardEulerSim.py {betta} {gamma} {deltaT} {timecap}')
   sys.exit() 

#initialize global variables
N = 1
I = .01
S = N - I
R=0
t = 0
timeCap = int(sys.argv[4])
betta = float(sys.argv[1])
gamma = float(sys.argv[2])
deltaT = float(sys.argv[3])

#Conntainers
sBucket = [S]
iBucket = [I]
iCalcBucket = [I]
rBucket = [R]
tBucket = [0]
t = 0

def displayResults():
    #plt.plot(tBucket, sBucket, label = "S taiske")
    plt.plot(tBucket, iBucket, label = "I")
    #plt.plot(tBucket, rBucket, label = "R taiske")
    plt.plot(tBucket, iCalcBucket, label = "I Calc")
    plt.legend()
    plt.title('SIS model with beta: {}  and gamma: {}; deltaT: {}'.format(betta, gamma, deltaT))
    plt.savefig('bruh')

def calcForwardStep():
    incidents = (betta * sBucket[-1] * iBucket[-1]) 
    recoveries = gamma * iBucket[-1] 
    print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    sDot = -incidents + recoveries
    iDot = incidents - recoveries
    rDot = recoveries
    return sDot, iDot,rDot 

def calcCalcStep():
    inverseRnot = 1 - (1/(betta / gamma))
    deltaLilI = (betta *  gamma) * iCalcBucket[-1] * (1 -(iCalcBucket[-1] / inverseRnot))
    iCalcBucket.append(iCalcBucket[-1] + deltaLilI)
def applyStepChanges(_sDot, _iDot, _rDot):
    sBucket.append(sBucket[-1] + (deltaT * _sDot))
    iBucket.append(iBucket[-1] + (deltaT * _iDot))
    rBucket.append(rBucket[-1] + (deltaT * _rDot))
    tBucket.append(tBucket[-1] + deltaT)
    
#Time loop
while t < timeCap:
    sDot, iDot, rDot = calcForwardStep()
    applyStepChanges(sDot, iDot, rDot)
    calcCalcStep()
    t += deltaT

displayResults()
