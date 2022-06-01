import unittest
import math

def tan_cf(x, k):
    def inner(x, i):
        if i == k:
            return (x * x) / (i * 2 - 1)
        else:
            return (x * x) /(i * 2 - 1 - inner(x, i + 1))
    return x / (1 - inner(x, 2))

class Test(unittest.TestCase):
    def test_equality(self):
        radians = math.radians(45)
        self.assertAlmostEqual(math.tan(radians), tan_cf(radians, 10), 4)

if __name__ == "__main__":
    unittest.main()