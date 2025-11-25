# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:51:11 2025

@author: karna
"""

def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
n=5
res=factorial(n)
print(res)