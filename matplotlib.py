import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def sinus():
    fig, axes = plt.subplots()
    x = np.linspace(-5,5,100)
    y = np.sin(x)
    plt.plot(x,y)
    axes.spines[["right","top"]].set_visible(False)
    axes.spines[["bottom","left"]].set_position("zero")
    plt.show()
def cosinus():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 100)
    y = np.cos(x)
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def tangent():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = np.tan(x)
    y[np.abs(y)>10] = np.nan
    print(y)
    plt.plot(x,y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def catangent():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = 1/np.tan(x)
    y[np.abs(y)>10] = np.nan
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def arcsin():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = np.arcsin(x)
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def arccos():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = np.arccos(x)
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def arctan():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = np.arctan(x)
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def arccotan():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = 3.1415926535/2 - np.arctan(x)
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def krug():
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = (25-x**2)**0.5
    plt.plot(x, y)
    plt.plot(x, -y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def kvadrat(v):
    fig, axes = plt.subplots()
    x = np.linspace(-v, v, 1000)
    a = [v for i in range(998)]
    a.insert(0, 0)
    a.append(0)
    y = np.array(a)
    plt.plot(x, y)
    plt.plot(x, -y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def parabola(v):
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y = v*x**2
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
def giperbola(v):
    fig, axes = plt.subplots()
    x = np.linspace(-5, 5, 1000)
    y =  abs(v)/x
    plt.plot(x, y)
    axes.spines[["right", "top"]].set_visible(False)
    axes.spines[["bottom", "left"]].set_position("zero")
    plt.show()
giperbola(-10)
