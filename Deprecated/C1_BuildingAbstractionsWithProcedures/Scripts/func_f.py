import unittest

def f_recursive(n):
    if n < 3:
        return n
    else:
        return f_recursive(n-1) + 2 * f_recursive(n-2) + 3 * f_recursive(n - 3)

def f_iterative(n):
    cache_fi = list()
    cache_fi.append(0)
    cache_fi.append(1)
    cache_fi.append(2)
    for i in range(3, n + 1):
        fi = cache_fi[i-1] + 2 * cache_fi[i-2] + 3 * cache_fi[i - 3]
        cache_fi.append(fi)
    return cache_fi[n]



class TestStringMethods(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(f_recursive(10), f_iterative(10))


if __name__ == "__main__":
    unittest.main()
