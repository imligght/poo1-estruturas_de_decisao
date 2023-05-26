# -*- coding: utf-8 -*-

A, B = input().split()

A = int(A)
B = int(B)

if (B % A == 0):
    
    print ("Sao Multiplos")
    
elif (A % B == 0):
    
    print ("Sao Multiplos")
    
else:
    
    print ("Nao sao Multiplos")