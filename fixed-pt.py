# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:59:40 2017

@author: jason
"""
import numpy as np
import matplotlib.pyplot as plt
import time

p = -0.5
eps = 10**-9

def g(x):
    #return (x**3 + 3*x**2 - 1) / -4
    return x**3 + 3*x**2 + 5*x - 1

def f(x):
    return x**3 + 3*x**2 + 4*x - 1
    
x = np.linspace(p-2,p+2)

while abs(g(p) - p) > eps:
    p = g(p)
    print(p)
    plt.plot(x,f(x))
    plt.scatter(p,f(p))
    plt.show()
    time.sleep(0.2)
