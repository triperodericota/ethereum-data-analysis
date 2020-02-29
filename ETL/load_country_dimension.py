#!/usr/bin/python3

import pandas as pd
import numpy as np


def load_dimension(connection_db):
    countrys = pd.read_csv("data_source/world-regions-according-to-the-world-bank.csv")
    currency_codes = pd.read_csv("data_source/iso_4217_currency_codes.csv")

    countrys = countrys.loc[:,['country','Code','World Region according to the World Bank']]
    currency_codes = currency_codes.loc[:,['Entity','Currency','Alphabetic_Code']]
    countrys.loc[:,'country'] = countrys.apply(lambda line: line.country.title(), 1)
    currency_codes.loc[:,'Entity'] = currency_codes.apply(lambda line: line.Entity.title(), 1)
    countrys_currency = pd.merge(currency_codes, countrys,  right_on='country', left_on='Entity', how='inner').drop("country",axis=1)
    ## rename columns to insert in DB
    countrys_currency = countrys_currency.rename(columns={'Entity':'name', 'Code': 'code', 'Currency': 'currency', 'World Region according to the World Bank': 'region', 'Alphabetic_Code': 'currency_code'})
    ## put withspace on rows without code
    countrys_currency=countrys_currency.fillna(value={'code':' '})
    ##  insert in database
    countrys_currency.to_sql("country_dimension", connection_db, if_exists='append', index=False)
