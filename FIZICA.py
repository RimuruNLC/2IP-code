import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
def dz(ugol,scorost):
    v = scorost/3.6
    fig, axes = plt.subplots()
    L = (v ** 2 * math.sin(2 * math.radians(ugol))) / 9.81
    x = np.linspace(0,L,10000)
    y = x * math.tan(math.radians(ugol)) - (9.81*x**2)/(2*v**2*math.cos(math.radians(ugol))**2)
    axes.plot(x,y)
    plt.plot(x,y)
    axes.spines[["right","top"]].set_visible(False)
    axes.spines[["bottom","left"]].set_position("zero")
    plt.show()
dz(65, 10)
