import unittest


def fringe(x, rl=[]):
    for i in range(0, len(x)):
        if type(x[i]) is not list:
            rl.append(x[i])
        else:
            fringe(x[i], rl)
    return rl


class Test(unittest.TestCase):
    def test_equality(self):
        x = [[1, 2], [3, 4]]
        self.assertEqual(fringe(x), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()