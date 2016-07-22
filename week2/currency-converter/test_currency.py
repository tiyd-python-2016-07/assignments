from currency import Currency, DifferentCurrencyCodeError
from nose.tools import assert_raises


def test_create_currency_with_amount_and_code():
     one_dollar = Currency(1, 'USD')

     assert one_dollar.amount == 1
     assert one_dollar.code == 'USD'


def test_create_usd_currency_with_value():
     one_dollar_twenty_cents = Currency('$1.20')

     assert one_dollar_twenty_cents.amount == 1.20
     assert one_dollar_twenty_cents.code == 'USD'


def test_create_euro_currency_with_value():
     seven_euros = Currency('€7.00')

     assert seven_euros.amount == 7.0
     assert seven_euros.code == 'EUR'


def test_currencys_can_be_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 == curr2


def test_currencys_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 != curr2


def test_currencys_with_different_currency_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert curr1 != curr2


def test_currencys_with_same_currency_codes_can_be_added():
    curr1 = Currency(4, 'USD')
    curr2 = Currency(3, 'USD')
    result = curr1 + curr2
    assert result == Currency(7, 'USD')


def test_adding_int_to_currency_returns_currency():
    result = 4 + Currency(3, 'USD')
    assert result == Currency(7, 'USD')


def test_adding_currency_to_int_returns_currency():
    result = Currency(3, 'USD') + 4
    assert result == Currency(7, 'USD')


def test_currencys_with_same_currency_codes_can_be_subtracted():
    curr1 = Currency(4, 'USD')
    curr2 = Currency(3, 'USD')
    result = curr1 - curr2
    assert result == Currency(1, 'USD')


def test_subtracting_int_from_currency_returns_currency():
    result = 4 - Currency(3, 'USD')
    print(result.amount)
    assert result == Currency(1, 'USD')


def test_subtracting_currency_to_int_returns_currency():
    result = Currency(4, 'USD') - 3
    assert result == Currency(1, 'USD')


def test_adding_currencys_with_different_currency_codes_raises_error():
    curr1 = Currency(4, 'USD')
    curr2 = Currency(3, 'EUR')
    with assert_raises(DifferentCurrencyCodeError):
        curr1 + curr2


def test_subtracting_currencys_with_different_currency_codes_raises_error():
    curr1 = Currency(4, 'USD')
    curr2 = Currency(3, 'EUR')
    with assert_raises(DifferentCurrencyCodeError):
        curr1 - curr2


def test_multiplying_currency_by_int_returns_currency():
    assert Currency(3, 'USD') * 3 == Currency(9, 'USD')


def test_multiplying_by_int_by_currency_returns_currency():
    assert 3 * Currency(3, 'USD') == Currency(9, 'USD')


def test_multiplying_by_int_by_currency_returns_currency():
    assert Currency(3, 'USD') * Currency(3, 'USD') == Currency(9, 'USD')
