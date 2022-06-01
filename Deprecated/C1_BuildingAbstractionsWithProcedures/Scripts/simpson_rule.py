import sys
sys.setrecursionlimit(10000)

def cube(a):
    return a * a * a

def y(f, a, h, k):
    return f(a + k * h)

def simpson_rule(f, a, b, n):
    h = (b - a)/n
    sum = 0
    for i in range(0, n + 1):
        sum += y(f, a, h, i)
    sum *= h
    return sum

def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def integral(f, a, b, dx):
    def add_dx(x):
        return x + dx
    return sum(f, a + dx / 2, add_dx, b) * dx

if __name__ == "__main__":
    print("integral:")
    print(integral(cube, 0, 1, 0.01))
    print(integral(cube, 0, 1, 0.001))
    print("simpson_rule:")
    print(simpson_rule(cube, 0, 1, 100))
    print(simpson_rule(cube, 0, 1, 1000))
