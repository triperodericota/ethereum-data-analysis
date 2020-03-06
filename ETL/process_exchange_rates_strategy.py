#!/usr/bin/python3

import pandas as pd
from abc import ABC, abstractmethod
import db_con
from datetime import datetime,date
from sqlalchemy import text
# import pdb

class AbstractReadingStrategy(ABC):
    # abstrtact class that represent interface to process the country's exchange rates files for and storage in database the processing result

    def __init__(self, file_path):
        self.__file = file_path
        self.__connection_db = db_con.db_connection()
        super().__init__()

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, a_file_path):
        self.__file_path=a_file_path

    @property
    def connection_db(self):
        return self.__connection_db

    @connection_db.setter
    def connection_db(self, a_connection):
        self.__connection_db = a_connection

    def retrieve_country(self,country_name):
        query = text("SELECT idcountry_dimension,name,currency,currency_code FROM country_dimension WHERE name=:country_name")
        query = query.bindparams(country_name=country_name)
        country = self.connection_db.execute(query).first()
        return country[0]

    def retrieve_date_id(self,date_value):
        query = text("SELECT date_id FROM date_dimension WHERE date=:value")
        date_id = self.connection_db.execute(query,value=date_value).first()
        return date_id[0]

    def insert_in_db(self, dataframe):
        dataframe.to_sql("usd_exchange_rates", self.connection_db, if_exists='append', index=False)

    @abstractmethod
    def read_file(self,country_name):
        #each subclass must be implemented this method
        pass


class InvestingCSVFilesReading(AbstractReadingStrategy):
# concrete class to read and process files from Investing.com

    def read_file(self,country_name):
        source = pd.read_csv(self.file, parse_dates=["Date"])
        source['Date'] = source['Date'].apply(pd.to_datetime)
        country_id = self.retrieve_country(country_name)
        exchange_rate_schema = {'country_id': [], 'value': [], 'date_id': [], 'date': []}
        for i in range(0,len(source.index)):
            exchange_rate = source.loc[i,['Date','Price']]
            #pdb.set_trace()
            exchange_rate_schema["date_id"].append(self.retrieve_date_id(exchange_rate.Date.date()))
            exchange_rate_schema["date"].append(exchange_rate.Date.date())
            exchange_rate_schema["value"].append(str(exchange_rate.Price).replace(",",""))
            exchange_rate_schema["country_id"].append(country_id)

        return pd.DataFrame(exchange_rate_schema)


class QuandlJSONFilesReading(AbstractReadingStrategy):
# concrete class to read and process files from Quandl API

    def read_file(self,country_name):
        df = pd.read_json(self.file)
        country_id = self.retrieve_country(country_name)
        data_frame_data = {'country_id': [], 'value': [], 'date_id': [], 'date': []}
        for exchange in df.loc['data'][0]:
                exchange_value = exchange[1]
                exchange_date = datetime.strptime(exchange[0],"%Y-%m-%d")
                exchange_date = date(exchange_date.year,exchange_date.month,exchange_date.day)
                data_frame_data['value'].append(exchange_value)
                data_frame_data['date_id'].append(self.retrieve_date_id(exchange_date))
                data_frame_data['date'].append(exchange_date)
                data_frame_data["country_id"].append(country_id)

        return pd.DataFrame(data_frame_data)
