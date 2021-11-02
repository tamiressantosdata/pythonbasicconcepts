# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:45:08 2021

@author: tamir
"""

import numpy as np
import scipy as sp
import numpy as np
from numpy import linalg
A = np.array([[3, -1, 4], [-1, 0, -1], [4, -1, 2]])
v, B = linalg.eig(A)
i = 0 # first eigenvalue/eigenvector pair
lambda0 = v[i]
print(lambda0)

x0 = B[:, i] # ith column of B
print(x0)
