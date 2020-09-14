def S1(a1=1,b1=2,c1=3,a2=2,b2=3,c2=4):
    d=a1*b2-a2*b1
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    return x,y



a1= int(input())
b1= int(input())
c1= int(input())
a2= int(input())
b2= int(input())
c2= int(input())


S1 = S1 (a1,b1,c1,a2,b2,c2)
print("x,y = ", S1 )
