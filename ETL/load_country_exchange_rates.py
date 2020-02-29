#!/usr/bin/python3

import pandas as pd
import numpy as np
import db_con
from datetime import datetime,date
from sqlalchemy import text

def retrieve_date_id(date_value):
    query = text("SELECT date_id FROM date_dimension WHERE date=:value")
    query = query.bindparams(value=date_value)
    date_id = db_con.db_connection().execute(query).first()
    return date_id[0]

connection_db = db_con.db_connection()
real_exchange_rates = pd.read_json("../data_source/quandl_data/brazilian_real.json")

country = real_exchange_rates.values[3][0]
query = text("SELECT country_id FROM country_dimension WHERE name=:country_name")
query = query.bindparams(country_name=country)
country_id = connection_db.execute(query).first()
country_id = country_id[0]
data_frame = {'country_id': [], 'value': [], 'date_id': []}
exchange_rates = real_exchange_rates.values[4][0]
for exchange in exchange_rates:
        exchange_value = exchange[1]
        exchange_date = datetime.strptime(exchange[0],"%Y-%m-%d")
        exchange_date = date(exchange_date.year,exchange_date.month,exchange_date.day)
        date_id = retrieve_date_id(exchange_date)
        data_frame['country_id'].append(country_id)
        data_frame['value'].append(exchange_value)
        data_frame['date_id'].append(date_id)

exchange_rate = pd.DataFrame(data_frame)
exchange_rate.to_sql("USDExchangeRates", connection_db, if_exists='append', index=False)
