# -*- coding: utf-8 -*-

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if (A + B <= C) or (A + C <= B) or (B + C <= A):
    
    print ("Invalido")
    
elif (A == B and A == C):
    
    print ("Valido-Equilatero")
    
    if (A ** 2 + B ** 2 == C ** 2) or (C ** 2 + A ** 2 == B ** 2) or (B ** 2 + C ** 2 == A ** 2):
        
        print ("Retangulo: S")
        
    else:
        
            print ("Retangulo: N")
        
elif (A + B > C) and (A + C > B) and (B + C > A):
    
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        
        print ("Valido-Isoceles")
        
        if (A ** 2 + B ** 2 == C ** 2) or (C ** 2 + A ** 2 == B ** 2) or (B ** 2 + C ** 2 == A ** 2):

            print ("Retangulo: S")

        else:

            print ("Retangulo: N")
        
    elif (A != B and A != C) and (B != A and B != C) and (C != A and C != B):
    
        print ("Valido-Escaleno")
 
        if (A ** 2 + B ** 2 == C ** 2) or (C ** 2 + A ** 2 == B ** 2) or (B ** 2 + C ** 2 == A ** 2):

            print ("Retangulo: S")

        else:

            print("Retangulo: N")