import sys
import unittest
sys.setrecursionlimit(10000)
import math

def cont_frac(n, d, k):
    def inner(n, d, i):
        if i == k:
            return n(k) / d(k)
        else:
            return n(i) / (d(i) + inner(n, d, i + 1))
    return n(1) / (d(1) + inner(n, d, 2))

def cont_frac_iterative(n, d, k):
    result = n(k) / d(k)
    for i in range(k - 1, 0, -1):
        result = n(i) / (d(i) + result)
    return result
        

class Test(unittest.TestCase):
    def test_equality(self):
        inverse_phi = 1 / (( 1 + math.sqrt(5) ) / 2)
        n = lambda i : 1.0
        d = lambda i : 1.0
        k = 11
        self.assertAlmostEqual(cont_frac(n, d, k), inverse_phi, 4)
        self.assertEqual(cont_frac(n, d, k), cont_frac_iterative(n, d, k))


if __name__ == "__main__":
    unittest.main()