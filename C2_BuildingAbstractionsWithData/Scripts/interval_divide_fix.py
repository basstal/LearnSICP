import unittest
from interval_width import *
from interval_bounds import *

def div_interval(x, y):
    if upper_bound(y) == 0 or lower_bound(y) == 0:
        raise Exception('divide by zero')
    return mul_interval(x, make_interval(1 / upper_bound(y), 1 / lower_bound(y)))

class Test(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(Exception):
            x = make_interval(-1, 0)
            y = make_interval(-1, 0)
            div_interval(x, y)

if __name__ == "__main__":
    unittest.main()