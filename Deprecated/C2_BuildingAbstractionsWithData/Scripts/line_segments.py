import unittest


def midpoint_segment(p0, p1):
    return make_point((x_point(p0) + x_point(p1)) / 2, (y_point(p0) + y_point(p1)) / 2)

def make_point(x, y):
    return {"x" : x, "y": y}

def x_point(p):
    return p["x"]

def y_point(p):
    return p["y"]


def print_point(p):
    print('\n')
    print("(")
    print(x_point(p))
    print(",")
    print(y_point(p))
    print(")")

class Test(unittest.TestCase):
    def test_equality(self):
        p0 = make_point(2, 10)
        p1 = make_point(10, 2)

        self.assertEqual(x_point(p0), 2)
        self.assertEqual(y_point(p0), 10)
        self.assertEqual(midpoint_segment(p0, p1), make_point(6, 6))

if __name__ == "__main__":
    unittest.main()
