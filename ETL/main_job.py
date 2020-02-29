#!/usr/bin/python3

# This file is the start point for ETL process
# Here, call to submodules(transformations) that load dimension and fact tables for Data Warehouse


import load_country_dimension as lcd
import load_date_dimension as ldd
import load_usd_exchange_rates_dimension as luerd
import load_DAI_transactions_dimension as ldtd
import db_con

connection_db = db_con.db_connection()

lcd.load_dimension(connection_db)
print("\n Country dimension loaded ")
ldd.load_dimension(connection_db)
print("\n Date dimension loaded ")
luerd.load_dimension()
print("\n USD_exchange_rates fact table loaded ")
ldtd.load_dimension(connection_db)
print("\n DAI_transactions fact table loaded ")
