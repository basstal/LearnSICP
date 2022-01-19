import unittest
from unittest.suite import TestSuite
import search_for_primes

def filtered_accumulate(combiner, null_value,  term,  a, next, b, filter):
    def iter(a, result):
        if a > b:
            return result
        else:
            return iter(next(a), combiner(term(filter(a, null_value)), result))
    return iter(a, null_value)


def add(a, b):
    return a + b

def sum_prime_square( a, b):
    def term(a):
        return a * a
    def next(a):
        return a+1
    def filter_is_prime(a, null_value):
        if search_for_primes.is_prime(a):
            return a
        else:
            return null_value
    return filtered_accumulate(add, 0, term, a, next, b, filter_is_prime)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def product_primes_to_n(n):
    def mul(a, b):
        return a*b
    def term(a):
        return a
    def next(a):
        return a+1
    def filter(a, null_value):
        if gcd(a, n) == 1:
            return a
        else:
            return null_value
    return filtered_accumulate(mul, 1, term, 1, next, n-1, filter)

class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(sum_prime_square(1, 20), 1027)
        self.assertEqual(search_for_primes.is_prime(1), False)
        self.assertEqual(gcd(7, 17), 1)
        self.assertEqual(gcd(125, 25), 25)
        self.assertEqual(product_primes_to_n(9), 2240)


if __name__ == "__main__":
    unittest.main()