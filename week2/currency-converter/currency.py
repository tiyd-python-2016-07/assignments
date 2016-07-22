class DifferentCurrencyCodeError(Exception):
    pass


class UnsupportedOtherType(TypeError):
    pass


class Currency:
    def __init__(self, amount, code=''):
        if isinstance(amount, (int, float)):
            self.amount = amount
            self.code = code
        elif isinstance(amount, str):
            self.amount = self.parse_amount(amount)
            self.code = self.parse_code(amount)
        else:
            raise TypeError("amount")

    def parse_amount(self, amount):
        return float(amount[1:])

    def parse_code(self, amount):
        code = amount[0]
        currency_code_map = {
            '$': 'USD',
            '€': 'EUR',
            '¥': 'JPY'
        }
        return currency_code_map[code]

    def __eq__(self, other):
        return self.amount == other.amount and \
            self.code == other.code

    def __add__(self, other):
        return Currency(self.amount + self.get_other_amount(other), self.code)

    def __sub__(self, other):
        return Currency(self.amount - self.get_other_amount(other), self.code)

    def __rsub__(self, other):
        return Currency(self.get_other_amount(other) - self.amount, self.code)

    def __mul__(self, other):
        return Currency(self.amount * self.get_other_amount(other), self.code)

    __radd__ = __add__
    __rmul__ = __mul__

    def get_other_amount(self, other):
        if isinstance(other, Currency):
            self.ensure_same_currencies(other)
            return other.amount
        elif isinstance(other, (int, float)):
            return other
        else:
            raise UnsupportedOtherType

    def ensure_same_currencies(self, other):
        if self.code != other.code:
            raise DifferentCurrencyCodeError
