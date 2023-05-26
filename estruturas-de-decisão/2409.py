# -*- coding: utf-8 -*-

A, B, C = input().split()
H, L = input().split()

A = int(A)
B = int(B)
C = int(C)
H = int(H)
L = int(L)

lista = [A, B, C]
lista.sort()

if (lista[0] <= L and lista[1] <= H) or (lista[1] <= L and lista[0] <= H):
        
        print ("S")
    
else:
    
    print ("N")