import sys
sys.setrecursionlimit(10000)
import time
import math
import random
import smallest_divisor as sd

def runtime():
    return time.time_ns()

def timed_prime_test(n):
    print('\n')
    print(n)
    return start_prime_test(n, runtime())

def start_prime_test(n, start_time):
    if is_prime(n):
        report_prime(runtime() - start_time)
        return True
    return False

def report_prime(elapsed_time):
    print(" *** ")
    print(elapsed_time)

def is_prime(n):
    if n == 1:
        return False
    return sd.smallest_divisor(n) == n

def search_for_primes(range_min, range_max):
    if range_min % 2 == 0:
        range_min += 1
    count = 0
    for n in range(range_min, range_max, 2):
        if timed_prime_test(n):
            count += 1
        if count == 3:
            break
"""
region Answer 1.24
"""
def fast_is_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_is_prime(n, times - 1)
    else:
        return False

def fermat_test(n):
    def try_it(a):
        return math.exp(a, n) % n == a
    return try_it(1 + random.randint(1, n - 1))

def timed_prime_test1(n):
    print('\n')
    print(n)
    return start_prime_test1(n, runtime())

def start_prime_test1(n, start_time):
    """
    times 这里是随便给的值
    here give a whatever value to times
    """
    if fast_is_prime(n, 999):
        report_prime(runtime() - start_time)
        return True
    return False
"""
endregion
"""

if __name__ == "__main__":
    """
    测试时计算速度过快导致结果 elapsed_time 都为 0
    elasped_time all 0 because of compute speed is too fast
    """
    search_for_primes(1001, 9999)
    search_for_primes(10001, 99999)
    search_for_primes(100001, 999999)
    search_for_primes(1000001, 9999999)
