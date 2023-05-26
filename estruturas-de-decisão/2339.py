# -*- coding: utf-8 -*-

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if ((B / A) >= C):
    
    print ("S")
    
elif ((B / A) < C):
    print ("N")