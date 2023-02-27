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
V = .5
S = N - I  - V
R=0
t = 0

betta = float(sys.argv[1])
gamma = float(sys.argv[2])
deltaT = float(sys.argv[3])
timeCap = int(sys.argv[4])

#Conntainers
sBucketLM = [[S],[S]]
sBucketANM =[[.5],[]] #[[N-I-.2*V],[S]]
iBucketLM = [[I],[I]]
iBucketANM = [[I],[I]]
rBucketLM = [[R], [R]]
rBucketANM = [[R], [R]]
vBucketANM = [[.2 * V], [.2 * V]]
vBucketLM =[[V], [V]]
tBucket = [0]
t = 0
def displayResults():
    plt.figure(figsize=(8,5))
    plt.plot(tBucket, sBucketANM[0], label = "s ANM",color='blue', linestyle='--')
    plt.plot(tBucket, iBucketANM[0], color='red', label = "i ANM", linestyle='--')
    plt.plot(tBucket, vBucketANM[0], color='black',label = "v ANM", linestyle='--')
    plt.plot(tBucket, rBucketANM[0],color='orange', label = "r ANM", linestyle='--')
    plt.plot(tBucket, sBucketLM[0], label = "s LM")
    plt.plot(tBucket, iBucketLM[0], color='red', label = "i LM")
    plt.plot(tBucket, vBucketLM[0], color='black',label = "v LM")
    plt.plot(tBucket, rBucketLM[0], label = "r LM", color='orange')
    plt.ylabel('Proportion of the Population')
    plt.xlabel('Time')
    plt.legend()
    plt.title('Leaky Vaccine vs All or Nothing Vaccine R0: {}'.format(betta/gamma))
    #plt.savefig('bruh')
    plt.show()

def calcForwardStepANM():
    incidents = (betta * sBucketANM[0][-1] * iBucketANM[0][-1])
    vDot = - (betta * vBucketANM[0][-1] * iBucketANM[0][-1])
    recoveries = gamma * iBucketANM[0][-1] 
    #print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    sDot = -incidents
    iDot = incidents - recoveries - vDot
    rDot = recoveries
    return sDot, iDot, rDot, vDot

def calcForwardStepLM():
    incidents = (betta * sBucketLM[0][-1] * iBucketLM[0][-1])
    recoveries = gamma * iBucketLM[0][-1] 
    vDot = -(betta * vBucketLM[0][-1] * iBucketLM[0][-1] * (.2))
    #print('Incidents: {} \nRecoveries: {}'.format(incidents, recoveries))
    sDot = -incidents
    iDot = incidents - recoveries - vDot
    rDot = recoveries
    return sDot, iDot,rDot, vDot

def applyStepChanges(_sDot, _iDot, _rDot,_vDot, target):
    if (target == "ANM"):
        sBucketANM[0].append(sBucketANM[0][-1] + (deltaT * _sDot))
        iBucketANM[0].append(iBucketANM[0][-1] + (deltaT * _iDot))
        rBucketANM[0].append(rBucketANM[0][-1] + (deltaT * _rDot))
        vBucketANM[0].append(vBucketANM[0][-1] + deltaT *  _vDot)
        tBucket.append(tBucket[-1] + deltaT)
    if (target  == 'LM'):
        sBucketLM[0].append(sBucketLM[0][-1] + (deltaT * _sDot))
        iBucketLM[0].append(iBucketLM[0][-1] + (deltaT * _iDot))
        rBucketLM[0].append(rBucketLM[0][-1] + (deltaT * _rDot))
        vBucketLM[0].append(vBucketLM[0][-1] + (deltaT * _vDot))
#Time loop
while t < timeCap:
    sDot, iDot, rDot, vDot = calcForwardStepANM()
    applyStepChanges(sDot, iDot, rDot,vDot, 'ANM')
    sDot, iDot, rDot, vDot  =  calcForwardStepLM()
    applyStepChanges(sDot, iDot, rDot, vDot, 'LM')
    t += deltaT

displayResults()
