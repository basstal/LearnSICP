import unittest


def deep_reverse(l):
    if type(l) is list:
        rl = []
        for i in range(0, len(l)):
            rl.insert(0, deep_reverse(l[i]))
        return rl
    return l

class Test(unittest.TestCase):
    def test_equality(self):
        l = [[1, 4], [9, 16, 25]]
        rl = deep_reverse(l)
        self.assertEqual(rl, [[25, 16, 9], [4, 1]])


if __name__ == "__main__":
    unittest.main()