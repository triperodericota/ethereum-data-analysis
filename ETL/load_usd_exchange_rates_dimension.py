#!/usr/bin/python3

from exchange_rates_for_country import ExchangeRateForCountry
import process_exchange_rates_strategy as proc


def load_dimension():
    # East Asia and Pacific countries
    #Australia
    exchange_rates_file = "data_source/exchange_rates/East Asia and Pacific/australian_dollar.json"
    australia_ec = ExchangeRateForCountry("Australia", proc.QuandlJSONFilesReading(exchange_rates_file))
    australia_ec.load_dimension()

    #PhilipineS
    philipines_ec = ExchangeRateForCountry("Philippines",proc.InvestingCSVFilesReading("data_source/exchange_rates/East Asia and Pacific/USD_PHP.csv"))
    philipines_ec.load_dimension()
