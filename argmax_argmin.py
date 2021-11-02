# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:53:46 2021

@author: tamir
"""

import numpy as np
import matplotlib.pyplot as plt

N = 100
L = 1

def f(i, n):
    x = i * L / N
    lam = 2*L/(n+1)
    return x * (L-x) * np.sin(2*np.pi*x/lam)

a = np.fromfunction(f, (N+1, 5))
min_i = a.argmin(axis=0)
max_i = a.argmax(axis=0)
plt.plot(a, c='k')
plt.plot(min_i, a[min_i, np.arange(5)], 'v', c='k', markersize=10)
plt.plot(max_i, a[max_i, np.arange(5)], '^', c='k', markersize=10)
plt.xlabel(r'$x$')
plt.ylabel(r'$f_n(x)$')
plt.show()
