import compose
import unittest

def square(x):
    return x * x

def repeated(f, n):
    r = f
    while n > 1:
        r = compose.compose(r, f)
        n = n - 1
    return r

class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(repeated(square, 2)(5), 625)
    
if __name__ == "__main__":
    unittest.main()