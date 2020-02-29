#!/usr/bin/python3

import pandas as pd
import numpy as np
from datetime import datetime,date
from sqlalchemy import text
import pdb

def retrieve_date_id(date_value,db_connection):
    query = text("SELECT date_id FROM date_dimension WHERE date=:value")
    date_id = db_connection.execute(query,value=date_value).first()
    return date_id[0]

def load_dimension(db_connection):

    #EXTRACT FROM SOURCE
    sai_txs = pd.read_csv("data_source/sai_transactions.csv")
    sai_txs = sai_txs.drop(columns=['nonce','block_hash','transaction_index','Unnamed: 0'])

    # TRANSFORMATIONS
    # calculate transaction fee = gas * gas_value (in Ether)
    sai_txs["transaction_fee"] = sai_txs.loc[:,["gas","gas_price"]].apply(lambda row: row["gas"] * row["gas_price"], axis=1)

    # transform block_timestamp to date
    sai_txs["date"] = sai_txs.loc[:,"block_timestamp"].apply(lambda row: pd.Timestamp(row, unit='s').date())
    # add date_id
    sai_txs["date_id"] = sai_txs.loc[:,"date"].apply(lambda row: retrieve_date_id(row,db_connection))

    # LOAD ADDRESS
    addresses = sai_txs["from_address"].unique()
    addresses = np.append(addresses,sai_txs["to_address"].unique())
    #print(address_df)
    # save address from sai's transactions in DataFrame to storage in database
    address_df = pd.DataFrame(addresses, columns=['address'])
    address_df.to_sql('address_dimension', db_connection, if_exists='append', index=False)

    #retrieve ids from address to manage this in memory and load dai's transactions
    addresses = db_connection.execute("SELECT * FROM address_dimension")

    dict_addresses = {}

    for row in addresses.fetchall():
        dict_addresses[row[1]] = row[0]

    sai_txs["from_address_id"] = sai_txs.loc[:,"from_address"].apply(lambda row: dict_addresses[row])
    # '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359' is sai's smart contract address
    sai_address_id = dict_addresses['0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359']
    sai_txs["to_address_id"] = sai_address_id

    sai_txs = sai_txs.drop(columns=['from_address','to_address'])
    # LOAD TO DATABASE
    sai_txs.to_sql("dai_transactions", db_connection, if_exists='append', index=False)
