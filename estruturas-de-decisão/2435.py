N, D, V = input().split()
N0, D0, V0 = input().split()

N = int(N)
D = int(D)
V = int(V)
N0 = int(N0)
D0 = int(D0)
V0 = int(V0)

TCN = (D / 1000) / V
TCN0 = (D0 / 1000) / V0

if (TCN > TCN0):
    
    print (f"{N0}")
    
elif (TCN < TCN0):
    
    print (f"{N}")