# -*- coding: utf-8 -*-

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if (A > B and A > C):
    
    if (B > C):
        
        print (f"{B}")
        
    elif (C > B):
            
        print (f"{C}")
            
if (B > A and B > C):
    
    if (A > C):
        
        print (f"{A}")
        
    elif (C > A):
            
        print (f"{C}")
            
if (C > B and C > A):
    
    if (B > A):

        print (f"{B}")

    elif (A > B):
        
        print (f"{A}")