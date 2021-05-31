import numpy as numpy
from matplotlib import pyplot as plt
from numpy.lib import math
from satellite import *
from constants import *
from colour import Color
import time

satellites = []
N = 3600

for counter in range(N):
    angle = 360/N*counter
    satellites.append(Satellite((Re+h, 0, np.pi/180*angle)))

angles = []
trajectories = []

for angle, sat in enumerate(satellites):
    sat.computePath()

    angleTemp = []
    pathTemp = []

    for n in sat.posArray:
        angleTemp.append(n[2])
        pathTemp.append(n[1])

    angles.append(angleTemp)
    trajectories.append(pathTemp)

colors = Color("blue").range_to(Color("green"), N)

colorshex = []

for c in colors:
    colorshex.append(c.hex)

device = (Re, np.pi/4, np.pi/5)

chords = []
centralAngles = []
timesOverPoint = []
distanceTable = []
minimums = []
inRange = []

for i, sat in enumerate(satellites):
    min = np.pi
    minIndex = -1
    distances = []

    for index, path in enumerate(sat.posArray):
        d = getGreatCircleDistance(device, path)
        distances.append(d)
        # print("calculating distances : " + str(index))

        if(d < min):
            min = d
            minIndex = index

    # if(not math.isnan(getIntersectionChordLength(min))):
    if(getIntersectionChordLength(min) < threshold):
        inRange.append(True)
        chords.append(getIntersectionChordLength(min))
    else:
        inRange.append(False)
        chords.append(0)

    distanceTable.append(distances)
    minimums.append((minIndex, min))

plt.figure(0)
plt.grid(True)
plt.ion()
plt.xlabel("longitude")
plt.ylabel("distance to the end-device")

for c in range(N):
    # plt.cla()
    plt.plot(distanceTable[c], color=colorshex[c])
    # plt.pause(.02)

for c in range(N):
    if(inRange[c]):
        plt.plot(minimums[c][0], minimums[c][1], color="g", marker='o')
    else:
        plt.plot(minimums[c][0], minimums[c][1], color='r', marker='o')

plt.ioff()

plt.figure(1)
plt.grid(True)
plt.ion()

for c in range(N):
    if(inRange[c] == True):
        plt.plot(c, minimums[c][1], 'g+')
    else:
        plt.plot(c, minimums[c][1], 'r+')

plt.ioff()

plt.figure(2)
plt.grid(True)

velocity = getVelocity(560e3, 4)
durationsOverDevice = []

for i, m in enumerate(minimums):
    newRadius = getRadiusOfNewCircle(m[1])
    newDepth = footprintPlaneDepth - (Re - newRadius)
    arcLength = getArcLengthFromPlaneDepth(newDepth)
    duration = arcLength/velocity
    durationsOverDevice.append(duration)

plt.plot(list(range(N)), durationsOverDevice)
plt.show()
