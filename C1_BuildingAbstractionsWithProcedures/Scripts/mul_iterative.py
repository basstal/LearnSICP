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


def mul_iterative(a, b):
    if a == 0:
        return 0
    
    mul_cache = list()
    while b != 1:
        while b % 2 == 0:
            mul_cache.append(b)
            b /= 2
        while b != 1 and b % 2 == 1:
            mul_cache.append(b)
            b -= 1
    cache = a
    while len(mul_cache) > 0:
        b = mul_cache.pop()
        if b % 2 == 0:
            cache = cache + cache
        else:
            cache = cache + a
    return cache

class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(mul_iterative(4, 25), mul(4, 25))
        self.assertEqual(mul_iterative(3, 22), mul(3, 22))
        self.assertEqual(mul_iterative(22, 4), mul(22, 4))
        self.assertEqual(mul_iterative(25, 3), mul(25, 3))


if __name__ == "__main__":
    unittest.main()