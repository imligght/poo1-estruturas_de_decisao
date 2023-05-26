# -*- coding: utf-8 -*-

CV, CE, CS, FV, FE, FS = input().split()

CV = int(CV)
CE = int(CE)
CS = int(CS)
FV = int(FV)
FE = int(FE)
FS = int(FS)

pontuacao_C = (CV * 3 + CE)
pontuacao_F = (FV * 3 + FE)

if (pontuacao_C > pontuacao_F):
    
    print ("C")
    
elif (pontuacao_C < pontuacao_F):
        
    print ("F")
        
elif (pontuacao_C == pontuacao_F):
    
    if (CS > FS):
        
        print ("C")
        
    elif (FS > CS):
            
        print ("F")
        
    elif (pontuacao_C == pontuacao_F and CS == FS):
    
        print ("=")

