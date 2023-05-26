# -*- coding: utf-8 -*-

n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if (media >= 7.0):
    
    print (f"Media: {media:.1f}")
    print ("Aluno aprovado.")
    
elif (media < 5.0):
    
    print (f"Media: {media:.1f}")
    print ("Aluno reprovado.")
    
elif (5.0 <= media <= 6.9):
    
    print (f"Media: {media:.1f}")
    print ("Aluno em exame.")
    
    nota_exame = float(input())
    
    print (f"Nota do exame: {nota_exame:.1f}")
    
    nota_final = (nota_exame + media) / 2
    
    if (nota_final >= 5.0):
        
        print ("Aluno aprovado.")
        print (f"Media final: {nota_final:.1f}")
    
    elif (nota_final <= 4.9):
        
        print ("Aluno reprovado.")
        print (f"Media final: {nota_final:.1f}")