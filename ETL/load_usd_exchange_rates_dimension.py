#!/usr/bin/python3

from exchange_rates_for_country import ExchangeRateForCountry
import process_exchange_rates_strategy as proc


def load_dimension():
    # East Asia and Pacific countries
    #Australia
    exchange_rates_file = "data_source/exchange_rates/East Asia and Pacific/australian_dollar.json"
    australia_ec = ExchangeRateForCountry("Australia", proc.QuandlJSONFilesReading(exchange_rates_file))
    australia_ec.load_dimension()
    #chinese_yuan
    china_ec = ExchangeRateForCountry("China", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/chinese_yuan.json"))
    china_ec.load_dimension()
    #hong_kong_dollar
    hong_kong_ec = ExchangeRateForCountry("Hong Kong", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/hong_kong_dollar.json"))
    hong_kong_ec.load_dimension()
    #japanese_yen
    japan_ec = ExchangeRateForCountry("Japan", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/japanese_yen.json"))
    japan_ec.load_dimension()
    #malaysian_ringgit
    malaysian_ec = ExchangeRateForCountry("Malaysia", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/malaysian_ringgit.json"))
    malaysian_ec.load_dimension()
    #new_zealand_dollar
    new_zealand_ec = ExchangeRateForCountry("New Zealand", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/new_zealand_dollar.json"))
    new_zealand_ec.load_dimension()
    #signapore_dollar
    singapore_ec = ExchangeRateForCountry("Singapore", proc.QuandlJSONFilesReading("data_source/exchange_rates/East Asia and Pacific/signapore_dollar.json"))
    singapore_ec.load_dimension()
    #PhilipineS
    philipines_ec = ExchangeRateForCountry("Philippines",proc.InvestingCSVFilesReading("data_source/exchange_rates/East Asia and Pacific/USD_PHP.csv"))
    philipines_ec.load_dimension()
    #Thailand
    thailand_ec = ExchangeRateForCountry("Thailand",proc.InvestingCSVFilesReading("data_source/exchange_rates/East Asia and Pacific/USD_THB.csv"))
    thailand_ec.load_dimension()
    #Indonesia
    indonesia_ec = ExchangeRateForCountry("Indonesia",proc.InvestingCSVFilesReading("data_source/exchange_rates/East Asia and Pacific/USD_IDR.csv"))
    indonesia_ec.load_dimension()
    #Mongolia
    mongolia_ec = ExchangeRateForCountry("Mongolia",proc.InvestingCSVFilesReading("data_source/exchange_rates/East Asia and Pacific/USD_MNT.csv"))
    mongolia_ec.load_dimension()

    #Europe and Central Asia
    #danish_krone
    danish_krone_ec = ExchangeRateForCountry("Denmark", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/danish_krone.json"))
    danish_krone_ec.load_dimension()
    #hungary_forint
    hungary_ec = ExchangeRateForCountry("Hungary", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/hungary_forint.json"))
    hungary_ec.load_dimension()
    #norwegian_krone
    norway_ec = ExchangeRateForCountry("Norway", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/norwegian_krone.json"))
    norway_ec.load_dimension()
    #pound_starling
    united_kingdom_ec = ExchangeRateForCountry("United Kingdom", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/pound_sterling.json"))
    united_kingdom_ec.load_dimension()
    #russian_ruble
    russian_ec = ExchangeRateForCountry("Russian", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/russian_ruble.json"))
    russian_ec.load_dimension()
    #swedish_krona
    sweden_ec = ExchangeRateForCountry("Sweden", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/swedish_krona.json"))
    sweden_ec.load_dimension()
    #swiss_franc
    switzerland_ec=ExchangeRateForCountry("Switzerland", proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/swiss_franc.json"))
    switzerland_ec.load_dimension()
    #Euro
    countries_with_euro_currency = ['Andorra','Austria','Belgium','Estonia','Finland','France','Germany','Greece','Ireland','Italy','Lithuania','Luxembourg','Netherlands','Portugal','Spain']
    for country in countries_with_euro_currency:
        euro_ec = ExchangeRateForCountry(country, proc.QuandlJSONFilesReading("data_source/exchange_rates/Europe and Central Asia/euro.json"))
        euro_ec.load_dimension()

    #Latin America and Caribbean
    #Argentina
    argentina_ec = ExchangeRateForCountry("Argentina", proc.InvestingCSVFilesReading("data_source/exchange_rates/Latin America and Caribbean/USD_ARS.csv"))
    argentina_ec.load_dimension()
    #Brazil
    brazil_ec = ExchangeRateForCountry("Brazil", proc.QuandlJSONFilesReading("data_source/exchange_rates/Latin America and Caribbean/brazilian_real.json"))
    brazil_ec.load_dimension()
    #mexico
    mexico_ec = ExchangeRateForCountry("Mexico", proc.QuandlJSONFilesReading("data_source/exchange_rates/Latin America and Caribbean/mexican_peso.json"))
    mexico_ec.load_dimension()
    #Costa Rica
    costa_rica_ec = ExchangeRateForCountry("Costa Rica", proc.InvestingCSVFilesReading("data_source/exchange_rates/Latin America and Caribbean/USD_CRC.csv"))
    costa_rica_ec.load_dimension()
    #Guatemala
    guatemala_ec = ExchangeRateForCountry("Guatemala", proc.InvestingCSVFilesReading("data_source/exchange_rates/Latin America and Caribbean/USD_GTQ.csv"))
    guatemala_ec.load_dimension()
    #Honduras
    honduras_ec = ExchangeRateForCountry("Honduras", proc.InvestingCSVFilesReading("data_source/exchange_rates/Latin America and Caribbean/USD_HNL.csv"))
    honduras_ec.load_dimension()
    #Nicaragua
    nicaragua_ec = ExchangeRateForCountry("Nicaragua", proc.InvestingCSVFilesReading("data_source/exchange_rates/Latin America and Caribbean/USD_NIO.csv"))
    nicaragua_ec.load_dimension()

    #North America
    canada_ec = ExchangeRateForCountry("Canada", proc.QuandlJSONFilesReading("data_source/exchange_rates/North America/canadian_dollar.json"))
    canada_ec.load_dimension()

    #South Asia
    #Afghanistan
    afghanistan_ec = ExchangeRateForCountry("Afghanistan", proc.InvestingCSVFilesReading("data_source/exchange_rates/South Asia/USD_AFN.csv"))
    afghanistan_ec.load_dimension()
    #India
    india_ec = ExchangeRateForCountry("India", proc.QuandlJSONFilesReading("data_source/exchange_rates/South Asia/indian_rupee.json"))
    india_ec.load_dimension()
    #Sri Lanka
    sri_lanka_ec = ExchangeRateForCountry("Sri Lanka", proc.QuandlJSONFilesReading("data_source/exchange_rates/South Asia/sri_lanka_rupee.json"))
    sri_lanka_ec.load_dimension()

    #Sub_saharan_africa
    #South africa
    south_africa_ec = ExchangeRateForCountry("South Africa", proc.QuandlJSONFilesReading("data_source/exchange_rates/Sub-Saharan Africa/south_africa_rand.json"))
    canada_ec.load_dimension()
    #Burundi
    burundi_ec = ExchangeRateForCountry("Burundi", proc.InvestingCSVFilesReading("data_source/exchange_rates/Sub-Saharan Africa/USD_BIF.csv"))
    burundi_ec.load_dimension()
    #Ethiopia
    ethiopia_ec = ExchangeRateForCountry("Ethiopia", proc.InvestingCSVFilesReading("data_source/exchange_rates/Sub-Saharan Africa/USD_ETB.csv"))
    ethiopia_ec.load_dimension()
    #Uganda
    uganda_ec = ExchangeRateForCountry("Uganda", proc.InvestingCSVFilesReading("data_source/exchange_rates/Sub-Saharan Africa/USD_UGX.csv"))
    uganda_ec.load_dimension()
    #XOF Currency
    countries_with_xof_currency = ['Togo', 'Senegal','Guinea-Bissau',"Cote D'Ivoire",'Burkina Faso','Benin']
    for country in countries_with_xof_currency:
        xof_ec = ExchangeRateForCountry(country, proc.InvestingCSVFilesReading("data_source/exchange_rates/Sub-Saharan Africa/USD_XOF.csv"))
        xof_ec.load_dimension()
    #XAF currency
    countries_with_xaf_currency = ['Cameroon','Central African Republic','Chad','Congo','Equatorial Guinea','Gabon']
    for country in countries_with_xaf_currency:
        xaf_ec = ExchangeRateForCountry(country, proc.InvestingCSVFilesReading("data_source/exchange_rates/Sub-Saharan Africa/USD_XAF.csv"))
        xaf_ec.load_dimension()
