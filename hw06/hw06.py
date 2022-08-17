passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value
        self.previous = None

    def next(self):
        if self.previous is None:
            result = Fib(1)
        else:
            result = Fib(self.value + self.previous.value)
        result.previous = self
        return result

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cash = 0
        self.stocks = 0

    def vend(self):
        if self.stocks > 0:
            if self.cash < self.price:
                return f'You must deposit ${self.price - self.cash} more.'
            else:
                change = self.cash - self.price
                self.cash = 0
                self.stocks -= 1
                return f'Here is your {self.name}' + (f' and ${change} change.' if change > 0 else '.')
        else:
            return 'Machine is out of stock.'

    def deposit(self, in_deposit):
        if self.stocks > 0:
            self.cash += in_deposit
            return f'Current balance: ${self.cash}'
        else:
            return f'Machine is out of stock. Here is your ${in_deposit}.'

    def restock(self, in_stocks):
        self.stocks += in_stocks
        return f'Current {self.name} stock: {self.stocks}'
