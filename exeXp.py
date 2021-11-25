# exercises 1

def abs ():
    """Returns the absolute value of the argument."""
    pass

def int ():
    """Returns the absolute value of the argument."""
    pass

def input ():
    """Returns the absolute value of the argument."""
    pass

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

# exercises 2

class Currency():
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
    
    def __iadd__(self, currency):
        return Currency(self.symbol, self.amount, currency.amount)
    
    def __add__(self, currency):
        return self.amount + currency.amount
    
    def __str__(self):
        return f'currency {self.symbol}, amount {self.amount}'

dollar_1 = Currency('$', 5)
dollar_2 = Currency('$', 5)

dollar_2 += dollar_1

dollar_string = str(dollar_1)

total = dollar_1

