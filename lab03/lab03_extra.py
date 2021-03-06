""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    return (
        lambda n: lambda x: x
        if n == 0
        else f1(x)
        if n == 1
        else f2(f1(x))
        if n == 2
        else f3(f2(f1(x)))
        if n == 3
        else cycle(f1, f2, f3)(n - 3)(f3(f2(f1(x))))
    )


## Lambda expressions


def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n


## More recursion practice


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def no_remainder(x):
        return x <= n // 2 and (no_remainder(x + 1) if n % x != 0 else True)

    return not no_remainder(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    def term(x):
        return odd_term(x) + even_term(x + 1) if x + 1 <= n else odd_term(x)

    def rec(x):
        return term(x) + rec(x + 2) if x + 2 <= n else term(x)

    return rec(1)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    def count_number(x, n):
        return (1 if n % 10 == x else 0) + count_number(x, n // 10) if n > 0 else 0

    def pair(x, n):
        return (
            count_number(x, n) * count_number(10 - x, n) + pair(x + 1, n)
            if x < 5
            
            else count_number(5, n) * (count_number(5, n) - 1) // 2
            if x == 5
            else 0
        )

    return pair(1, n)
