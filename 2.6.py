def S2(N=72000):
    x=N%3600
    y=x//60
    return y


N= int(input())
S2 = S2 (N)
print(" = ", S2 )
