# -*- coding: utf-8 -*-

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

soma1 = B + C
soma2 = A + B
soma3 = A + C

if (A < soma1 and B < soma3 and C < soma2):
    
    perimetro = A + B + C

    print (f"Perimetro = {perimetro:.1f}")
    
else:
    
    area = (A + B) / 2 * C
    
    print (f"Area = {area:.1f}")