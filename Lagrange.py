# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:23:07 2021

@author: gansa001
"""
from sympy import *
import math


def delta(j,a,x,N):
    '''
    Parameters
    ----------
    j : int. 
        the jth lagrange polynomial
    a : sympy symbol
        the dependent term in the lagrange polynomial
    x : list
        x values from the original function
    N : int

    Returns
    -------
    The lagrange polynomial for any given j

    '''
    num=1
    den=1
    for i in range(N):
        if i!=j:
            num*=(a-x[i])
            den*=(x[j]-x[i])
    return (num/den)


def Lagrange(x,y):
    '''
    Parameters
    ----------
    x : list
        dependent variable values
    y : list
        independent variable values

    Returns
    -------
    The lagrangian approximation of the function

    '''
    N=len(x)
    a=Symbol('a')
    f=0
    for j in range(len(x)):
        answer= (delta(j,a,x,N))
        f+=y[j]*answer
    return (simplify(f))



#test
'''
enter corresponding x and y values of the function to approximate.
In this case, the exponential function from -3 to 3
'''
x=[-3,-2,-1,0,1,2,3]
y=[math.exp(i) for i in x]

print(Lagrange(x,y))
