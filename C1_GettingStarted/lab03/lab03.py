""" Lab 3: Recursion and Midterm Review """


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    return (
        gcd(a, b % a)
        if b > a and b % a != 0
        else a
        if b % a == 0
        else gcd(b, a % b)
        if a % b != 0
        else b
    )


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    return (
        print(n)
        or (n == 1 and 1)
        or (hailstone(n // 2) if n % 2 == 0 else hailstone(n * 3 + 1)) + 1
    )
