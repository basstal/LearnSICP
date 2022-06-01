import unittest


def find_ijk(n, s):
    r = []
    for i in range(1, n):
        jk_set = find_ij(n, s - i)
        for pair in jk_set:
            if pair[0] != i and pair[1] != i:
                r.append((i, pair[0], pair[1]))
    return r


def find_ij(n, s):
    r = []
    for i in range(1, n):
        if s - i <= n and s - i > 0 and s - i != i:
            r.append((i, s - i))
    return r


class Test(unittest.TestCase):

    def test_equality(self):
        self.assertTrue((1, 2, 4) in find_ijk(10, 7))
        self.assertTrue((7, 9, 3) in find_ijk(10, 19))
        self.assertTrue(len(find_ijk(10, 31)) == 0)


if __name__ == "__main__":
    unittest.main()