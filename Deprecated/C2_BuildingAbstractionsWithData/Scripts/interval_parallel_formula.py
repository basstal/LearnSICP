from random import random
import unittest
from interval_width import *

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    return div_interval(one, add_interval(div_interval(one, r1), div_interval(one, r2)))

class Test(unittest.TestCase):
    def test_equality(self):
        while True:
            x = make_interval(random(), random())
            y = make_interval(random(), random())
            z = div_interval(x, y)
            w = div_interval(x, x)
            self.assertEqual(par1(x, y), par2(x, y))
            self.assertEqual(par1(z, w), par2(z, w))
            self.assertEqual(par1(x, x), par2(x, x))

if __name__ == "__main__":
    unittest.main()