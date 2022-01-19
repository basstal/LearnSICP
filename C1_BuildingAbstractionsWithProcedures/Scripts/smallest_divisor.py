def smallest_divisor(n):
    return find_divisor(n, 2)

def square(n):
    return n* n


def find_divisor(n, test_divisor):
    if square(test_divisor) > n:
        return n
    elif is_divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor+1)

def is_divides(a, b):
    return b % a == 0

"""
region Answer 1.23
"""
def find_divisor1(n, test_divisor):
    if square(test_divisor) > n:
        return n
    elif is_divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor1(n, next(test_divisor))

def next(test_divisor):
    if test_divisor == 2:
        return 3
    else:
        return test_divisor + 2
"""
endregion
"""

if __name__ == "__main__":
    print(smallest_divisor(199)) # 199
    print(smallest_divisor(1999)) # 1999
    print(smallest_divisor(19999)) # 7