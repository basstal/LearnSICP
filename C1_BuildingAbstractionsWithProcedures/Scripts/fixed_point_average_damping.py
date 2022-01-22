import math

tolerance = 0.00001

def fixed_point(f, first_guess):
    def is_close_enough(v1, v2):
        global tolerance
        return abs(v1 - v2) < tolerance
    def _try(guess, step):
        next = f(guess)
        print(f"step {step}, next guess {next}")
        if is_close_enough(guess, next):
            return next
        else:
            return _try(next, step + 1)
    return _try(first_guess, 1)


def with_average_damping():
    print("with_average_damping")
    def f(x):
        return (x + math.log(1000)/ math.log(x))/ 2
    return fixed_point(f, 2.0)

def without_average_damping():
    print("without_average_damping")
    def f(x):
        return math.log(1000) / math.log(x)
    return fixed_point(f, 2.0)


if __name__ == "__main__":
    print(with_average_damping())
    print(without_average_damping())
    