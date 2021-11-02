# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:50:06 2021

@author: tamir
"""

#basic arrays methods
import numpy as np

a = np.linspace(1, 4, 4)

print(a)
b = a.reshape(2, 2)
print(b)

b[0, 0] = -99

print(b)

print(a)


a = np.linspace(1, 6, 6). reshape(3, 2)
print(a)

a.transpose()

print(a.transpose())
b = np.array([101, 102, 103, 104])
print(b)
b.transpose()

print(b)
b.transpose()

print(b.transpose()) # transpose for one dimensional array  returns unchanged 

a=np.array([0,0,0,0])
b=np.array([1,1,1,1])
c=np.array([2,2,2,2])
np.vstack((a,b,c))
print(np.vstack((a,b,c))) #stack arrays vertically
np.hstack((a,b,c))
print(np.hstack((a,b,c))) #horizontally 
np.dstack((a,b,c))
print(np.dstack((a,b,c)))

a = np.arange (6)

print(a)
np.hsplit(a,3)
print(np.hsplit(a,3))
print(np.hsplit(a,(2,3,5)))

a=np.ones((3,3))
print(a)

np.vstack((a, np.array ((2, 2, 2))))
print(np.vstack((a, np.array ((2, 2, 2)))))

a=np.ones((3,3))
print(a)
b=np.array((2,2,2))
print(b)
c=b.reshape(3,1)
print(b.reshape(3,1))
np.hstack((a,c))
print(np.hstack((a,c)))

d=np.linspace(1,12,12).reshape(4,3)
print(d)
d[2, :] 
print(d[2, :] )
d[3,1]
print(d[3,1])
print(d[:,1])
print(d[:,0])
print( d[1:-1, 1:])
d[:, 1] = 0
print(d) ## set all elements in the second column to zero

#advanced indexing 
a=np.linspace(0,0.5,6)
print(a)
ai=[1,4,5]
print(a[ai])
ia=np.array(((1,2),(3,4)))
print(a[ia])