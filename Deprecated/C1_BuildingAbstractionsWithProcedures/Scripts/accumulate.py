import unittest

def accumulate(combiner, null_value,  term,  a, next, b):
    def iter(a, result):
        if a > b:
            return result
        else:
            return iter(next(a), combiner(term(a), result))
    return iter(a, null_value)

def accumulate_iterative(combiner, null_value,  term,  a, next, b):
    result = null_value
    while a <= b:
        result = combiner(term(a), result)
        a = next(a)
    return result


def add(a, b):
    return a + b
    
def mul(a, b):
    return a * b

def sum(term, a, next, b):
    return accumulate(add, 0, term, a, next, b)

def product(term, a, next, b):
    return accumulate(mul, 1, term, a, next, b)

def sum_iterative(term, a, next, b):
    return accumulate_iterative(add, 0, term, a, next, b)

def product_iterative(term, a, next, b):
    return accumulate_iterative(mul, 1, term, a, next, b)

def term(a):
    return a

def next(a):
    return a+1

class Tests(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(sum(term, 1, next, 255), 32640)
        self.assertEqual(product(term, 1, next, 15), 1307674368000)
        self.assertEqual(sum_iterative(term, 1, next, 255), 32640)
        self.assertEqual(product_iterative(term, 1, next, 15), 1307674368000)

if __name__ == "__main__":
    unittest.main()