# -*- coding: utf-8 -*-

code, amount = input().split()
code = int(code)
amount = int(amount)

if (code == 1):
    total = amount * 4.00

elif (code == 2):
    total = amount * 4.50

elif (code == 3):
    total = amount * 5.00
    
elif (code == 4):
    total = amount * 2.00
    
elif (code == 5):
    total = amount * 1.50
    
print(f"Total: R$ {total:.2f}")