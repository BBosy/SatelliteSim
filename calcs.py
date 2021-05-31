import constants as cs
import math
import numpy as np

distance_to_sat = cs.getDistanceToSatellite(10)
triangle_alt = cs.getTriangleAltitude(cs.Re+cs.h, distance_to_sat, cs.Re)
alpha = np.arcsin(triangle_alt/cs.Re) * 2

v = cs.getVelocity()
w = cs.getAngularVelocity(v)
T = cs.getOrbitalPeriod(w)

time_over_device = alpha/(2*np.pi) * T
