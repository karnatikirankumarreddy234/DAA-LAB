# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:58:29 2025

@author: karna
"""

def factorial(n):
    if(n==0):
         return 1
    else:
         return(n*factorial(n-1))
n=5
res= factorial(n)
print(res)
