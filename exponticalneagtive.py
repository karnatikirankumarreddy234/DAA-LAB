# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:37:52 2025

@author: karna
"""

def power(base,exponent):
    if(exponent==0):
        return 1
    else:
        return base*power(base, exponent-1)
base= 2
exponent= -5
res= power (base,abs(exponent))
if (exponent<0) :
    res=1/res
    print(res)


