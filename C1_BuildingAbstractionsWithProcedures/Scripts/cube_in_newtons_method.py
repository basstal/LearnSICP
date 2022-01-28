import unittest
import fixed_point_average_damping

dx = 0.00001

def deriv(g):
    global dx
    return lambda x : (g(x + dx) - g(x)) / dx

def newton_transform(g):
    return lambda x : x - (g(x) / (deriv(g)(x)))

def newtons_method(g, guess):
    return fixed_point_average_damping.fixed_point(newton_transform(g), guess)

def cubic(a, b, c):
    return lambda x : x * x * x + a * x * x  + b * x + c

class Test(unittest.TestCase):
    def test_equality(self):
        g = cubic(0, 0, 0)
        r = newtons_method(g, 1.0)
        self.assertAlmostEqual(g(r), 0)
        g = cubic(3, 2, 1)
        r = newtons_method(g, 1.0)
        self.assertAlmostEqual(g(r), 0)

if __name__ == "__main__":
    unittest.main()