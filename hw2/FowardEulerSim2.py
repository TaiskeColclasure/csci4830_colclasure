import matplotlib.pyplot as plt
import numpy as np
import sys
import  math


if(len(sys.argv) != 5):
    print('Usage: python3 ForwardEulerSim2.py {betta} {gamma} {deltaT} {timeCap}')
    sys.exit()

#initialize global variables
N = 1
I = .01
S = N - I
R=0
t = 0

betta = float(sys.argv[1])
gamma = float(sys.argv[2])
deltaT = float(sys.argv[3])
timeCap = int(sys.argv[4])

#Conntainers
sBucket = [S]
iBucket = [I]
iCalcBucket = [I]
rBucket = [R]
tBucket = [0]
errorMax = 0
t = 0
#reusedcalc
inverseRnot = 1/(betta/gamma)
inverseRnot  = 1 - inverseRnot
def displayResults():
    #plt.plot(tBucket, sBucket, label = "S taiske")
    plt.ylim(0,.5)
    plt.plot(tBucket, iBucket, color='red', label = "I Euler")
    plt.plot(tBucket, iCalcBucket, color='black',label = "I Analytical", linestyle='--')
    #plt.plot(tBucket, rBucket, label = "R taiske")
    plt.legend()
    plt.title('SIS model with beta: {}  and gamma: {}: deltaT: {}'.format(betta, gamma, deltaT))
    plt.savefig('bruh')

def calcForwardStep():
    incidents = (betta * sBucket[-1] * iBucket[-1])
    recoveries = gamma * iBucket[-1] 
    #print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    sDot = -incidents
    iDot = incidents - recoveries
    rDot = recoveries
    return sDot, iDot,rDot 

def calcCalcResult(_t):
    num = inverseRnot
    complexFrac = (inverseRnot - iBucket[0]) / (iBucket[0])
    eTerm = math.e ** (-(betta - gamma) * _t)
    denum = 1 + complexFrac * eTerm
    return num / denum
def applyStepChanges(_sDot, _iDot, _rDot):
    sBucket.append(sBucket[-1] + (deltaT * _sDot) + (deltaT* _rDot))
    iBucket.append(iBucket[-1] + (deltaT * _iDot))
    rBucket.append(rBucket[-1] + (deltaT * _rDot))
    tBucket.append(tBucket[-1] + deltaT)
    
#Time loop
while t < timeCap:
    sDot, iDot, rDot = calcForwardStep()
    applyStepChanges(sDot, iDot, rDot)
    calcResult = calcCalcResult(t)
    error = abs(iBucket[-1] - calcResult)
    errorMax = error if error > errorMax else errorMax
    iCalcBucket.append(calcResult)
    t += deltaT

displayResults()
print(errorMax)
