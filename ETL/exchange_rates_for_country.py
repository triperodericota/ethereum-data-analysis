#!/usr/bin/python3

class ExchangeRateForCountry():
# this class represents the client to load the exchange rates for each country
# for this, it's associating with strategy/ies to process data source and persist data in database


    def __init__(self,name,processing_strategy):#currency,currency_code,):
        self.__name = name
#        self.__currency = currency
#        self.__currency_code = currency_code
        #self.region(region)
#        self.__file_exchange_rates = file_exchange_rates
        self.__processing_strategy = processing_strategy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,a_name):
        self.__name=a_name

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self,a_currency):
        self.__currency=a_currency

    @property
    def currency_code(self):
        return self.__currency_code

    @currency_code.setter
    def currency_code(self,a_currency_code):
        self.__currency_code=a_currency_code

    @property
    def file_exchange_rates(self):
        return self.__file_exchange_rates

    @file_exchange_rates.setter
    def file_exchange_rates(self, a_file):
        self.__file_exchange_rates= a_file

    @property
    def processing_strategy(self):
        return self.__processing_strategy

    @processing_strategy.setter
    def processing_strategy(self, a_strategy):
        self.__processing_strategy = a_strategy

    def load_dimension(self):
        dataframe = self.processing_strategy.read_file(self.name)
        self.processing_strategy.insert_in_db(dataframe)
