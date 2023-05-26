# -*- coding: utf-8 -*-

L, A, P, R = input().split()

L = int(L)
A = int(A)
P = int(P)
R = int(R)

D = R*2
DP = (L ** 2 + A ** 2 + P ** 2) ** 0.5

if (D >= DP):
    
    print ("S")
    
else:
    
    print ("N")