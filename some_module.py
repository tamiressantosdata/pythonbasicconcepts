# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:27:12 2022

@author: tamir
"""

PI = 3.14159
def f(x):
 return x + 2

def g(a, b):
 return a + b



import some_module
result = some_module.f(5)
pi = some_module.PI



from some_module import f, g, PI
result = g(5, PI)