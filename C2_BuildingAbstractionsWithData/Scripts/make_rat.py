import unittest

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def make_rat(n, d):
    g = gcd(n, d)
    n = n / g if n^d > 0 or (n^d < 0 and n > 0) else -n / g
    return (n, abs(d / g))

class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(make_rat(1, 2), (1, 2))
        self.assertEqual(make_rat(7, 70), (1, 10))
        self.assertEqual(make_rat(7, -70), (-1, 10))
        self.assertEqual(make_rat(-7, -70), (1, 10))


if __name__ == "__main__":
    unittest.main()