import unittest
from interval_sub import *
from interval_bounds import *

def interval_width(x):
    return (upper_bound(x) - lower_bound(x)) / 2

def add_interval(x, y):
    return make_interval(lower_bound(x) + lower_bound(y), upper_bound(x) + upper_bound(y))

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    return mul_interval(x, make_interval(1 / upper_bound(y), 1 / lower_bound(y)))

class Test(unittest.TestCase):
    def test_equality(self):
        x = make_interval(-3, 3)
        y = make_interval(-4, 4)
        v0 = interval_width(add_interval(x, y))
        v1 = interval_width(x) + interval_width(y)
        self.assertEqual(v0, v1)
        v0 = interval_width(sub_interval(x, y))
        v1 = interval_width(x) - interval_width(y)
        self.assertEqual(v0, v1)

        v0 = interval_width(mul_interval(x, y))
        v1 = interval_width(x) * interval_width(y)
        self.assertNotEqual(v0, v1)
        v0 = interval_width(div_interval(x, y))
        v1 = interval_width(x) / interval_width(y)
        self.assertNotEqual(v0, v1)

if __name__ == "__main__":
    unittest.main()