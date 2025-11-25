# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 08:52:24 2025

@author: karna
"""

def binarysearch(arr,l,r,key):
    mid=(l+r)//2
    if(r>=l):
       if(key==arr[mid]):
           return mid
       elif(key<arr[mid]):
           return binarysearch(arr, l, mid-1 ,key)
       else:
           return binarysearch(arr,mid+l, r, key)
    else:
           return -1
       
        
arr=[1,2,3,5,8,4,1,3,5,13]
key=9
l=0
r=len(arr)-1
print(binarysearch(arr, l, r, key))