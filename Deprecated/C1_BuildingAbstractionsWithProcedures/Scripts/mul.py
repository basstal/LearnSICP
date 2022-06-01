import unittest

def halve(a):
    return a/2

def mul(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return mul(a, halve(b)) + mul(a, halve(b))
    else:
        return mul(a, b - 1) + a


def mul_origin(a, b):
    if b == 0:
        return 0
    else:
        return mul_origin(a, b - 1) + a


class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(mul_origin(4, 25), mul(4, 25))
        self.assertEqual(mul_origin(4, 22), mul(4, 22))


if __name__ == "__main__":
    unittest.main()