import unittest


def reverse(l):
    rl = []
    for i in range(0, len(l)):
        rl.insert(0, l[i])
    return rl

class Test(unittest.TestCase):
    def test_equality(self):
        l = [1, 4, 9, 16, 25]
        rl = reverse(l)
        self.assertEqual(rl, [25, 16, 9, 4, 1])


if __name__ == "__main__":
    unittest.main()