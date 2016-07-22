from currency import Currency

class UnknownCurrencyCodeError(Exception):
    pass


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, currency, to_code):
        if currency.code == to_code:
            return currency
        else:
            if to_code in self.rates:
                conversion_rate = self.rates[to_code]
                amount = currency.amount * conversion_rate
                return Currency(amount, to_code)
            else:
                raise UnknownCurrencyCodeError
