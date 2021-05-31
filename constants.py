import numpy as np
import math

G = 6.67408e-11
Me = 5.972e24
Ms = 4
Re = 6371e3
h = 560e3

footprintPlaneDepth = 1078e3
satelliteTangentLength = 2729e3
footprintPlaneRadius = 2518e3
gamma = 1.1661
gamma2 = 1.13194
threshold = 1665e3


def getDistanceToSatellite(epsilon, rad=False):
    return Re*(np.sqrt(((Re+h)/Re)**2-np.cos(epsilon)**2)-np.sin(epsilon)) if rad else Re*(np.sqrt(((Re+h)/Re)**2-np.cos(float(epsilon)/180*np.pi)**2)-np.sin(float(epsilon)/180*np.pi))


def getTriangleAltitude(a, b, c):
    # return np.arctan((a**2+b**2-c**2)*(a**2-b**2+c**2))
    area = 0.25*math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))
    return 2*area/a


def getVelocity(height=h, mass=Ms):
    return np.sqrt(G*(Me+mass)/(Re + height))


def getAngularVelocity(v, height=h):
    return v/(Re + height)


def getOrbitalPeriod(av):
    return 2*np.pi / av


def getFootprintPlaneDepth(L):
    centralAngle = np.arcsin(L/Re)
    depth = Re * (1 - np.cos(centralAngle))
    return depth


def getChordDistanceToCircle(angle):
    d = Re * (1 - np.cos(angle))
    return d


def getRadiusOfNewCircle(angle):
    i = getChordDistanceToCircle(angle)
    r = Re - i
    return r


def getArcLengthFromPlaneDepth(d):
    alpha = np.arccos(1-d/Re)
    L = alpha * Re
    return L
