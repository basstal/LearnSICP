import sys
"""
because python have recursion limit default to 100.
this will cause a procedural process fail.
change its limit to 10000 to prevent this failure.
因为递归数量超出 100 的限制，这里抬高这个限制
"""
sys.setrecursionlimit(10000)

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
    newguess = average(guess, (x / guess))
    print(newguess)
    return newguess

def average(x, y):
    return (x + y ) / 2

def square(x):
    return x * x
    
def good_enough(guess, x):
    good_enough = abs(square(guess) - x) < 0.001
    print(good_enough)
    return good_enough

def sqrt(x):
    return sqrt_iter(1.0, x)


"""
use new_if to replace the if in process sqrt_iter.
尝试用 new_if 替代 sqrt_iter 的 if
"""

def new_if(predicate, the_clause, else_clause):
    if predicate:
        return the_clause
    else:
        return else_clause

def sqrt_iter2(guess, x):
    """
    due to applicative-order evaluation problem, can't end the recursion even if process good_enough have returned true。
    因为 applicative-order 求值的问题导致这里无法在 good_enough 得到 true 后结束递归。
    """
    return new_if(good_enough(guess, x), guess, sqrt_iter2(improve(guess, x), x))

def sqrt2(x):
    return sqrt_iter2(1.0, x)


"""
Exercise 1.7

test -> 0.2147483648
result -> 0.4637124381035601
result3 -> 0.46340959907136087 (better)

test -> 9990.2147483648
result -> 99.95106201931117
result3 -> 99.9510617670708 (better)
"""

previous_guess = 0

def sqrt_iter3(guess, x):
    if good_enough2(guess):
        return guess
    else:
        return sqrt_iter3(improve(guess, x), x)

def good_enough2(guess):
    global previous_guess
    good_enough = abs(guess - previous_guess) < 0.001
    previous_guess = guess
    return good_enough

def sqrt3(x):
    global previous_guess
    previous_guess = 0
    return sqrt_iter3(1.0, x)