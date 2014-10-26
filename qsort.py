# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:08:15 2013

@author: zhihuixie
"""
import random
def quicksort(array_A):
    #global count
    lesser, greater=[],[]
    
    if array_A==[]:
        return []
    else:
        pivot=random.choice(array_A)
        L=array_A.index(pivot)
        
        for element in array_A[L+1:]+array_A[:L]:
            if element<pivot:
                lesser.append(element)
            else:
                greater.append(element)
        return quicksort(lesser)+[pivot]+quicksort(greater)

a=[2,3,8,4,5,0,9,1,7]
b=[0]
#print a+b
print quicksort(a)
