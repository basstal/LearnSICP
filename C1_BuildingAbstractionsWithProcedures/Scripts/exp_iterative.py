import math
import unittest

def square(a):
    return a * a


def fast_expt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_expt(b, n / 2))
    else:
        return b * fast_expt(b, n - 1)

def exp_iterative(b, n):
    if n == 0:
        return 1
    
    exp_cache = list()
    while n != 1:
        while n % 2 == 0:
            exp_cache.append(n)
            n /= 2
        while n != 1 and n % 2 == 1:
            exp_cache.append(n)
            n -= 1
    cache = b
    while len(exp_cache) > 0:
        n = exp_cache.pop()
        if n % 2 == 0:
            cache = cache * cache
        else:
            cache = b * cache
    return cache


class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(exp_iterative(4, 25), fast_expt(4, 25))
        self.assertEqual(exp_iterative(4, 22), fast_expt(4, 22))


if __name__ == "__main__":
    unittest.main()