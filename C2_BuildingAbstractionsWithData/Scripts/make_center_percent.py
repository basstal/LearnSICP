
import unittest
from interval_width import *
from interval_bounds import *


def make_center_percent(c, pw):
    return make_interval((c - c * pw), (c + c * pw))

def center(i):
    return (lower_bound(i) + upper_bound(i)) / 2

def width(i):
    return (upper_bound(i) - lower_bound(i)) / 2

def percent(x):
    return width(x) / center(x)


class Test(unittest.TestCase):
    def test_equality(self):
        x = make_center_percent(6.8, 1 / 10)
        self.assertAlmostEqual(percent(x), 1/10)

if __name__ == "__main__":
    unittest.main()