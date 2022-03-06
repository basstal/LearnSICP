import unittest

def same_parity(*args):
    rl = [args[0]]
    val = args[0] % 2
    for arg in args[1:]:
        if arg % 2 == val:
            rl.append(arg)
    return rl



class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(same_parity(1, 2, 3,4,5,6,7), [1,3,5,7])
        self.assertEqual(same_parity(2,3,4,5,6,7), [2,4,6])

if __name__ == "__main__":
    unittest.main()