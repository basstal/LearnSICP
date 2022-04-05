import unittest
from adjoin_set_ordered import *


def union_set(set1, set2):
    if set1 is None or len(set1) == 0:
        return set2
    elif set2 is None or len(set2) == 0:
        return set1
    elif set1[0] < set2[0]:
        r = [set1[0]]
        r.extend(union_set(set1[1:], set2))
        return r
    elif set1[0] == set2[0]:
        r = [set1[0]]
        r.extend(union_set(set1[1:], set2[1:]))
        return r
    else:
        r = [set2[0]]
        r.extend(union_set(set1, set2[1:]))
        return r


class Test(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(union_set([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
