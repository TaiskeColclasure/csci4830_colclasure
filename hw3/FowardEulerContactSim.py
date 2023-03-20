import matplotlib.pyplot as plt
import numpy as np
import sys
import  math


#if(len(sys.argv) != 5):
#    print('Usage: python3 ForwardEulerSim2.py {betta} {gamma} {deltaT} {timeCap}')
#    sys.exit()

#initialize global variables
N = 1
I = .001
S = N - I
R=0
t = 0

betta = 4
gamma = 3
deltaT = .25
timeCap = 25

#Conntainers
sBucket = [[S], [S], [S], [S]]
iBucket = [[I], [I], [I], [I]]
iCalcBucket = [[S], [S], [S], [S]]
rBucket = [[0], [0], [0], [0]]
tBucket = [0]
errorMax = 0
t = 0
cBar = 0.45
#reusedcalc
inverseRnot = 1/(betta/gamma)
inverseRnot  = 1 - inverseRnot
def displayResults():
    plt.plot(tBucket, iBucket[0], color='purple',alpha=.2, label = "I Euler")
    plt.plot(tBucket, iBucket[1], color='purple',alpha=.4, label = "I Euler")
    plt.plot(tBucket, iBucket[2], color='purple',alpha=.5, label = "I Euler")
    plt.plot(tBucket, iBucket[3], color='purple',alpha=.8, label = "I Euler")
    plt.legend()
    plt.title('SIS model with beta: {}  and gamma: {}: deltaT: {}'.format(betta, gamma, deltaT))
    plt.show()

def calcForwardStep():
    pMatrix = np.diag([1,2,3,4])
    iMatrix = np.matrix([iBucket[0][-1], iBucket[1][-1], iBucket[2][-1], iBucket[3][-1]])
    sDiag = np.diag([sBucket[0][-1], sBucket[1][-1], sBucket[2][-1], sBucket[3][-1]])
    cMatrix = np.full((4,4), cBar)
    omegDiag = np.diag([.25, .25, .25, .25])
    inverseDiag = np.linalg.inv(omegDiag)
    parenPt1 = np.matmul(sDiag, cMatrix)
    parenPt2 = np.matmul(parenPt1, inverseDiag)
    iGamma = np.matrix(gamma * iMatrix.A)
    sDot  = np.matmul(iMatrix, parenPt2)
    sDot = np.matmul([-1], np.matmul(sDot, pMatrix))
    iDot = np.subtract(sDot, iGamma)
    rDot = iGamma

    return sDot, iDot, rDot

def calcCalcResult(_t):
    num = inverseRnot
    complexFrac = (inverseRnot - iBucket[0]) / (iBucket[0])
    eTerm = math.e ** (-(betta - gamma) * _t)
    denum = 1 + complexFrac * eTerm
    return num / denum

def applyStepChanges(_sDot, _iDot, _rDot):
    sBucket[0].append(sBucket[0][-1] + (deltaT * _sDot.A.tolist()[0][0]))
    sBucket[1].append(sBucket[1][-1] + (deltaT * _sDot.A.tolist()[0][1]))
    sBucket[2].append(sBucket[2][-1] + (deltaT * _sDot.A.tolist()[0][2]))
    sBucket[3].append(sBucket[3][-1] + (deltaT * _sDot.A.tolist()[0][3]))

    iBucket[0].append(iBucket[0][-1] + (deltaT * _iDot.A.tolist()[0][0]))
    iBucket[1].append(iBucket[1][-1] + (deltaT * _iDot.A.tolist()[0][1]))
    iBucket[2].append(iBucket[2][-1] + (deltaT * _iDot.A.tolist()[0][2]))
    iBucket[3].append(iBucket[3][-1] + (deltaT * _iDot.A.tolist()[0][3]))

    rBucket[0].append(rBucket[0][-1] + (deltaT * _rDot.A.tolist()[0][0]))
    rBucket[1].append(rBucket[1][-1] + (deltaT * _rDot.A.tolist()[0][1]))
    rBucket[2].append(rBucket[2][-1] + (deltaT * _rDot.A.tolist()[0][2]))
    rBucket[3].append(rBucket[3][-1] + (deltaT * _rDot.A.tolist()[0][3]))

    tBucket.append(tBucket[-1] + deltaT)
    
#Time loop
while t < timeCap:
    sDot, iDot, rDot = calcForwardStep()
    applyStepChanges(sDot, iDot, rDot)
    t += deltaT

displayResults()
print(errorMax)
