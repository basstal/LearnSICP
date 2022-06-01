import unittest


def element_of_set(x, set):
    if set is None or len(set) == 0:
        return False
    elif x == set[0]:
        return True
    else:
        return element_of_set(x, set[1:])


def adjoin_set(x, set):
    set.append(x)
    return set


def intersection_set(set1, set2):
    if set1 is None or len(set1) == 0 or set2 is None or len(set2) == 0:
        return []
    elif element_of_set(set1[0], set2):
        r = [set1[0]]
        r.extend(intersection_set(set1[1:], set2))
        return r
    else:
        return intersection_set(set1[1:], set2)

def union_set(set1, set2):
    if set1 is None or len(set1) == 0:
        return set2
    elif set2 is None or len(set2) == 0:
        return set1
    elif element_of_set(set1[0], set2):
        return union_set(set1[1:], set2)
    else:
        r = [set1[0]]
        r.extend(union_set(set1[1:], set2))
        return r


class Test(unittest.TestCase):
    def test_equality(self):
        set = [1,1,3,3,5,7,9]
        self.assertEqual(element_of_set(1, set), True)
        self.assertEqual(element_of_set(2, set), False)
        self.assertEqual(adjoin_set(11, set), [1,1,3,3,5,7,9,11])
        self.assertEqual(intersection_set([], set), [])
        self.assertEqual(intersection_set(None, set), [])
        self.assertEqual(intersection_set([5,7,8], set), [5,7])
        self.assertEqual(union_set([5,7,8], set), [8,1,1,3,3,5,7,9,11])


if __name__ == "__main__":
    unittest.main()