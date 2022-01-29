# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:49:23 2022

@author: tamir
"""
#Basic Statistics 


import numpy as np 
arr = np.random.randn(5, 4)
print(arr)
arr.mean()
print(arr.mean())

arr.sum()
print(arr.sum)
arr.mean(axis=1)
print(arr.mean(axis=1))

arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr)
arr1.cumsum()
print(arr1.cumsum())


arr2 = np.random.randn(6)
print(arr2)
print(arr2.sort())


