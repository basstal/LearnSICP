import math

tolerance = 0.00001

def fixed_point(f, first_guess):
    def is_close_enough(v1, v2):
        global tolerance
        return abs(v1 - v2) < tolerance
    def _try(guess):
        next = f(guess)
        if is_close_enough(guess, next):
            return next
        else:
            return _try(next)
    return _try(first_guess)

def phi(x):
    return 1 + 1/x


if __name__ == "__main__":
    print(fixed_point(math.cos, 1.0))
    print(fixed_point(phi, 1.0))