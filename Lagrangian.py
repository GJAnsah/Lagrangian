# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:23:07 2021

@author: gansa001
"""
from sympy import *
import math

def delta(j,a,x,N):
    num=1
    den=1
    for i in range(N):
        if i!=j:
            num*=(a-x[i])
            den*=(x[j]-x[i])
    return (num/den)

def Lagarange(x,y):
    N=len(x)
    a=Symbol('a')
    f=0
    for i in range(len(x)):
        answer= (delta(i,a,x,N))
        f+=y[i]*answer
    return (simplify(f))

#test
x=[-3,-2,-1,0,1,2,3]
y=[math.exp(i) for i in x]


print(Lagarange(x,y))
