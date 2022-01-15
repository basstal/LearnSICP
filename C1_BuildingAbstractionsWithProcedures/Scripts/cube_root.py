import unittest

def cube_root_iter(guess, x):
    if good_enough(guess):
        return guess
    else:
        return cube_root_iter(improve(guess, x), x)

def improve(guess, x):
    newguess = (x / (guess * guess) + 2 * guess) / 3
    print(newguess)
    return newguess

previous_guess = 0

def good_enough(guess):
    global previous_guess
    good_enough = abs(guess - previous_guess) < 0.001
    previous_guess = guess
    return good_enough

def cube_root(x):
    global previous_guess
    previous_guess = 0
    return cube_root_iter(1.0, x)


class TestStringMethods(unittest.TestCase):
    def test_cube_root(self):
        root_val = cube_root(25.0)
        self.assertAlmostEqual(25.0, root_val * root_val * root_val, 5)

if __name__ == '__main__':
    unittest.main()