import unittest


def element_of_set(x, set):
    if set is None or len(set) == 0:
        return False
    elif set[0] == x:
        return True
    elif x < set[0]:
        return False
    else:
        return element_of_set(x, set[1:])


def adjoin_set(x, set):
    # print(f"x : {x}, set : {set}")
    if set is None or len(set) == 0:
        return [x]
    elif set[0] == x:
        return set
    elif x < set[0]:
        set.insert(0, x)
        return set
    else:
        r = [set[0]]
        r.extend(adjoin_set(x, set[1:]))
        return r


class Test(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(adjoin_set(1, [1, 3, 5]), [1, 3, 5])
        self.assertEqual(adjoin_set(2, [1, 3, 5]), [1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()