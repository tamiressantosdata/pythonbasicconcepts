# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:13:00 2021

@author: tamir
"""
import numpy as np 

a=np.array([-2,-1,0,1,2])
print(a)
ia=np.array([False, True, False,True, False])
print(a[ia])

ib=a>0

print(a[ib])

a[ib]=0 ## set all positive elements to zero
print(a)

a = np.array ([1, 2, 3])
b = np.array ([0, 10, 100])


print(a*b)

a=np.array([[1,2,3],[4,5,6]])
b=2
print(a*b)

b=np.array([1,2,3])
c=a*b
print(a)
print(c)

#sorting an array

a = np.array ([5, -1, 2, 4, 0, 4])

a.sort()
print(a)
#sort the numbers by columns
b=np.array ([[0 , 3, -2], [7, 1, 3], [4, 0, -1]])
print(b)
b.sort(axis=0)
print(b)

a = np.array ([3, 0, -1, 1])

print()
np.argsort(a)
print(np.argsort(a))#returns the indexes that would sort an array

#therefore
a[np.argsort(a)]

print( a[np.argsort(a)])


#shape into a column vector 
r = np.array ([3, 4, 5])
print(r)
c = r[:, np.newaxis]
print(c)

#logical comparisons
a= np.array([1.66e-27, 1.38e-23, 6.63e-34, 6.02e23 , np.nan ])
b = np.array ([1.66e-27, 1.66e-27, 1.66e-27, 6.00e23 , np.nan ])
np.isclose(a, b)
print(np.isclose(a, b))

x= np.linspace (0, np.pi , 100)
s=np.allclose(np.sin(x)**2 , 1 - np.cos(x)**2)
print(s)







