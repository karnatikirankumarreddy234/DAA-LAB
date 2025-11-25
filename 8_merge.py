# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 08:18:24 2025

@author: karna
"""

def merge(left,right):
    merge=[]
    i=j=0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            merge.append(left[i])
            i=i+1
        else:
          merge.append(right[j])
          j=j+1
    while(i<len(left)):
         merge.append(left[i])
         i=i+1
    while(j<len(right)):
        merge.append(right[j])
        j=j+1
    return merge