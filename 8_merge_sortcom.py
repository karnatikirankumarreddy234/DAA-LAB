# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 08:28:02 2025

@author: karna
"""

def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=int(len(arr)/2)
    left=arr[: mid]
    right=arr[mid :]
    mergesort(left)
    mergesort(right)
    return (merged(left, right))

def merged(left,right):
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


arr=[2,7,4,1,5,3,6]
print(mergesort(arr))