# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:41:17 2021

@author: tamir
"""

#Meshes in python 



import numpy as np 

x = np.linspace (0, 5, 6)
print(x)
y = np.linspace (0, 3, 4)
print(y)

X,Y=np.meshgrid(x,y)

print(X)
print(Y)