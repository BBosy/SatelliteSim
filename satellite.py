import numpy as np
from constants import *
from matplotlib import pyplot as plt
import time

w = 0.0010941119344718274


class Satellite:
    def __init__(self, pos0=(Re+h, 0, 0)):
        self.pos = pos0
        self.posArray = [self.pos]

    def computePath(self, step=1):
        deltaW = w/step
        while(self.posArray[-1][1] < np.pi):
            self.posArray.append(
                (Re+h, self.posArray[-1][1]+deltaW, self.pos[2]))
        # return self.posArray


def getGreatCircleDistance(p1, p2):
    alpha = np.arccos(np.sin(p1[1]) * np.sin(p2[1]) + np.cos(p1[1])
                      * np.cos(p2[1]) * np.cos(np.abs(p1[2]-p2[2])))
    distance = 2*Re*np.sin(alpha/2)
    # return distance
    return alpha


'''don't know what it does'''
# def getIntersectionChordLength(distance):
#     alpha = np.arccos(distance/L)
#     chordLength = 2 * np.sin(alpha/2) * L
#     return chordLength


def getIntersectionChordLength(alpha):
    chordLength = np.sin(alpha) * Re
    return chordLength


def chord2angle(d):
    angle = 2 * np.arcsin(d/(2*Re))
    return angle


def getTimeOverPoint(angle):
    return angle/w




'''
sat = Satellite()
sat.computePath()

device = (Re, np.pi/4, np.pi/5)

min = np.pi * Re
minIndex = 0

X = []

for i, x in enumerate(sat.posArray):
    d = getGreatCircleDistance(x, device)
    X.append(d)
    # print(d)
    if(d < min):
        min = d
        minIndex = i

# print(min)

chordLength = getIntersectionChordLength(min)
centralAngle = chord2angle(chordLength)
time = getTimeOverPoint(centralAngle)

print("the satellite spends " + str(time) + " seconds over the end device")

plt.plot(X, 'b-')
plt.plot(minIndex, min, 'ro')
plt.show()
'''
