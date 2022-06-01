def fold_left(op, initial, sequence):

    def iter(result, rest):
        if len(rest) == 0:
            return result
        else:
            return iter((op(result, rest[0])), rest[1:])

    return iter(initial, sequence)


def fold_right(op, initial, sequence):

    def iter(result, rest):
        if len(rest) == 0:
            return result
        else:
            return op(iter(result, rest[1:]), rest[0])

    return iter(initial, sequence)


def div(a, b):
    return a / b


def append_list(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if type(a) is list:
        a.append(b)
        return a
    elif type(b) is list:
        b.append(a)
        return b
    else:
        return [a, b]


if __name__ == "__main__":
    print(fold_right(div, 1, [1, 2, 3]))
    print(fold_left(div, 1, [1, 2, 3]))
    print(fold_right(append_list, None, [1, 2, 3]))
    print(fold_left(append_list, None, [1, 2, 3]))