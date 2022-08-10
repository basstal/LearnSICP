""" Optional problems for Lab 6 """

# Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    index = 0

    def vending_cycle():
        nonlocal index
        result = snacks[index]
        index = index + 1 if index < len(snacks) - 1 else 0
        return result
    return vending_cycle
