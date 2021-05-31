import matplotlib.pyplot as plt
import numpy as np

plt.ion()

for i in range(10):
    plt.scatter(i, i)
    plt.pause(0.5)
