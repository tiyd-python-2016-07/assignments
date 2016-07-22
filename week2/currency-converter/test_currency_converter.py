from currency import Currency
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from nose.tools import assert_raises


conversion_rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}

def test_create_converter_with_conversion_rates():
    converter = CurrencyConverter(conversion_rates)
    assert converter.rates == conversion_rates


def test_convert_with_same_code_returns_itself():
    # Arrange
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'USD'
    # Act
    result = converter.convert(currency, convert_to_code)
    # Assert
    assert result == Currency(1, 'USD')


def test_convert_with_different_code_returns_converted_currency():
    # Arrange
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'JPY'
    # Act
    result = converter.convert(currency, convert_to_code)
    # Assert
    assert result == Currency(120, 'JPY')


def test_convert_with_unknown_code_raises_error():
    # Arrange
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'FOO'

    with assert_raises(UnknownCurrencyCodeError):
        converter.convert(currency, convert_to_code)
