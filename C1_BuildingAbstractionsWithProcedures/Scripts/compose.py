import unittest

def square(x):
    return x * x

def inc(x):
    return x + 1

def compose(f, g):
    return lambda x : f(g(x))


class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(compose(square, inc)(6), 49)
        
if __name__ == "__main__":
    unittest.main()
