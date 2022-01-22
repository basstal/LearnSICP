import cont_frac_expression
import unittest
import math

n = lambda i : 1.0

def d(i):
    if i % 3 == 2:
        if i < 3:
            return 2
        else:
            return (i + 1) / 3 * 2
    return 1

class Test(unittest.TestCase):
    def test_equality(self):
        self.assertAlmostEqual(math.e, cont_frac_expression.cont_frac(n, d, 11) + 2, 4)

if __name__ == "__main__":
    unittest.main()