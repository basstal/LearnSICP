import unittest


def equal(a, b):
    if type(a) == type(b):
        t = type(a)
        if t is list and len(a) > 0:
            return equal(a[0], b[0]) and equal(a[1:], b[1:])
        else:
            return a == b


class Test(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(equal(["1", "2", "3"], ["1", "2", "3"]))
        self.assertTrue(not equal(["1", "2", "3"], [1, 2, 3]))
        self.assertTrue(not equal(1, 2))
        self.assertTrue(equal(2, 2))


if __name__ == "__main__":
    unittest.main()