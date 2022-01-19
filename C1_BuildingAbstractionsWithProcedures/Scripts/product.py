import unittest
import sys

sys.setrecursionlimit(1000000)

def product(next, start, end):
    result = 1
    while start <= end:
        result *= start
        start = next(start)
    return result

def product_recursive(next, start, end):
    if start <= end:
        return start * product_recursive(next, next(start), end)
    return 1
    
def next(a):
    return a+2

def pi_approximations(product, n):
    pi = (product(next, 2, n) * product(next, 4, n - 2)) / \
         (product(next, 3, n) * product(next, 3, n)) * 4
    return pi

class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(pi_approximations(product, 1000), \
            pi_approximations(product_recursive, 1000))


if __name__ == "__main__":
    unittest.main()
