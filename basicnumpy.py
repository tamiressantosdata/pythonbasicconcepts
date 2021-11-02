# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:43:28 2021

@author: tamir
"""


import numpy as np 
#using linspace 
x,dx = np.linspace (0., 2*np.pi , 100, retstep=True)
print(dx)

x = np.linspace (0, 5, 5, endpoint=False)

print(x)

#initializing array from a function 

def f(i,j):
    return 2*i*j

np.fromfunction(f,(4,3))
print(np.fromfunction(f,(4,3)))

#or using lambda function 

np. fromfunction (lambda i,j: 2*i*j, (4 ,3))

print(np.fromfunction( lambda i,j:2*i*j, (4,3)))
x = np.linspace (1, 5, 5)
print(x)

print(x**2)
print(x-1)
print(np.sqrt(x-1))
y = np.exp(-np.linspace (0., 2., 5))

print(y)

print(np.sin(x-y))

a=np.array(((1,2),(3,4)))
print(a)
b=a
print(a*b)

a=np.linspace(1,6,6)**3
print(a)
print(a>100)
print((a < 10) | (a > 100))
a /= 0 
print(a)
np.isnan(a)
print (np.isnan(a))
print(np.isinf(a))

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

b= a.flatten()  #flattened copy of a
print(b)
b[3]=0
print (b)

#resize and and  reshaped

a=np.linspace(1,4,4)
print(a)
print(a.resize(2,2))

#array creation 
np.arange (7)
print(np.arange(7))

np.arange (1.5 , 3., 0.5)
print(np.arange (1.5 , 3., 0.5))

np.zeros([3,3])
print(np.zeros([3,3]))

np.ones([3,3])
print(np.ones([3,3]))

#bystrings 
