def A(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return  2
    else:
        return A(x - 1, A(x, y - 1))

def f(n):
    return A(0, n)

def g(n):
    return A(1, n)

def h(n):
    return A(2, n)

if __name__ == "__main__":
    print(A(1, 10))
    print(A(2, 4))
    print(A(3, 3))
"""
    f(n) = 2n
    g(n) = 2^n
    h(n) = 2^(2^(2^(2...))) up to n times 一共n个2
"""