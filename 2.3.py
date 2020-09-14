def f1(x):
    f1 =x**4
    return f1


def f2(x):
    f2=4**x
    return f2

x = int(input())
Fx = f1(x)+f2(x)

y = int(input())
Fy = f1(y)+f2(y)

print("Fx = ", Fx)
print("Fy = ", Fy)
