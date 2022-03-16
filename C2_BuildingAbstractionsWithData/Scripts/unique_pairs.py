import sys
import random
import unittest

sys.setrecursionlimit(10000)


def unique_pairs(n):
    r = []
    for i in range(1, n):
        for j in range(1, i):
            r.append([i, j])
    return r


def accumulate(op, initial, sequence):
    if sequence is None or len(sequence) == 0:
        return initial
    else:
        return op(sequence[0], accumulate(op, initial, sequence[1:]))


def append_list(list1, list2):
    if list1 is None or len(list1) == 0:
        return list2
    else:
        return [list1[0], append_list(list1[1:], list2)]


def append_flat(list1, list2):
    r = []
    if list1 is not None:
        for e in list1:
            r.append(e)
    if list2 is not None:
        for e in list2:
            r.append(e)
    return r


def flatmap(proc, seq):
    r = []
    for elem in seq:
        r.append(proc(elem))
    # print("r = ", r)
    return accumulate(append_flat, None, r)


def fast_is_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_is_prime(n, times - 1)
    else:
        return False


def fermat_test(n):

    def try_it(a):
        assert (a < n)
        return a**n % n == a

    return try_it(random.randint(1, n - 1))


def is_prime_sum(pair):
    # print("pair = ", pair)
    return fast_is_prime(pair[0] + pair[1], 999)


def make_pair_sum(pair):
    return [pair[0], pair[1], pair[0] + pair[1]]


def filter_prime_pair(proc, fm):
    r = []
    for pair in fm:
        if proc(pair):
            r.append(pair)
    return r


def prime_sum_pairs(n):

    def enumerate_interval(b, e):
        r = []
        for i in range(b, e):
            r.append(i)
        return r

    def walk_i(i):
        r = []
        for j in enumerate_interval(1, i):
            r.append([i, j])
        return r

    fm = flatmap(walk_i, enumerate_interval(1, n))
    # print("fm = ", fm)
    r = filter_prime_pair(is_prime_sum, fm)
    prime_pairs = []
    for i in r:
        prime_pairs.append(make_pair_sum(i))
    return prime_pairs


def prime_sum_pairs_simple(n):

    # def enumerate_interval(b, e):
    #     r = []
    #     for i in range(b, e):
    #         r.append(i)
    #     return r

    # def walk_i(i):
    #     r = []
    #     for j in enumerate_interval(1, i):
    #         r.append([i, j])
    #     return r

    # fm = flatmap(walk_i, enumerate_interval(1, n))
    # print("fm = ", fm)
    r = filter_prime_pair(is_prime_sum, unique_pairs(n))
    prime_pairs = []
    for i in r:
        prime_pairs.append(make_pair_sum(i))
    return prime_pairs

class Test(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(prime_sum_pairs(10), prime_sum_pairs_simple(10))

if __name__ == "__main__":
    unittest.main()