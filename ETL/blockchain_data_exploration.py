#!/usr/bin/python3

import pandas as pd
import numpy as np
import os

# data visualization
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns


sai_address_contract = '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359'

def is_sai_txs(row):
    if(row["from_address"] == sai_address_contract):
        return True
    elif(row["to_address"] == sai_address_contract):
        return True
    else:
        return False

def read_blockchain_txs():
    # WARNING: transactions.csv size's ~ 6 GB, therefore the read sentence migth be very slow (depending of machine resource's)
    transactions = pd.read_csv("data_source/transactions.csv")
    #plot porcentage of sai/not sai's transactions (it's migth be slow too)
    transactions['type'] = transactions.apply(lambda row: is_sai_txs(row), axis=1)
    transactions['type'].value_counts().plot.pie(autopct='%1.1f%%', ax=axes[1])
    return transactions

if(os.path.exists("data_source/sai_transactions.csv")):
    sai_txs = pd.read_csv("data_source/sai_transactions.csv")
else:
    transactions = read_blockchain_txs()
    sai_txs = transactions[(transactions.from_address == sai_address_contract) | (transactions.to_address == sai_address_contract)]
    #save sai transactions to manipulate this file (it's much smaller than all transactions)
    sai_txs.to_csv("/home/triperodericota/Facultad/Tecnologias aplicadas a BI/TP Final/ETL/data_source/sai_transactions.csv")

#sai's stadistics
print("\n SAI's stadistics")
print(sai_txs.info())
print("\n Numerical variables: \n")
print(sai_txs.describe().T)
print("\n Categorical variables: \n")
print(sai_txs.describe(include=[np.object]).T)

from_addresses=sai_txs.groupby('from_address')
from_addresses.from_address.value_counts()

to_addresses = sai_txs.groupby('to_address')
to_addresses.to_address.value_counts()

sai_txs["from_sai_smart_contract_address"] = sai_txs["from_address"].apply(lambda row: True if sai_address_contract in row else False)
sai_txs["to_sai_smart_contract_address"] = sai_txs["to_address"].apply(lambda row: True if sai_address_contract in row else False)

# check missing values
print("\n Missing values in to_sai_smart_contract_address:")
print(sai_txs["to_sai_smart_contract_address"].isna().any())
print("\n Missing values in from_sai_smart_contract_address:")
print(sai_txs["from_sai_smart_contract_address"].isna().any())

# we can see that all SAI's transactions has sai's smart contract address as "to_address" column. This means that all sai's transfers go to sai's # smart contract address

print(sai_txs["to_sai_smart_contract_address"].all())
print(sai_txs["from_sai_smart_contract_address"].all())

print("\n Total SAI's transfers in dataset: " + str(sai_txs.size))
print("\n Total holders in dataset: " + str(sai_txs["from_address"].unique().size) + "addresses")
print("\n Total value tranfered in Wei: " + str(sai_txs["value"].sum()))

print("\n Mean gas in all transactions: " + str(sai_txs["gas"].mean()))
print("\n Max/min value for gas: " + str(sai_txs["gas"].max()) + "/" + str(sai_txs["gas"].min()))
#correlation between gas and gas_price
scatter_gas = sai_txs.plot.scatter('gas','gas_price')
scatter_gas.set_title('correlation between gas/gas_price')
plt.show()

print("\n Total blocks in SAI's transactions: " + str(sai_txs["block_hash"].unique().size))
print("\n Start block number:" + str(sai_txs["block_number"].min()) + " / End block number:" + str(sai_txs["block_number"].max()))
# calculate transaction fee = gas * gas_value (in Ether)
sai_txs["transaction_fee"] = sai_txs.loc[:,["gas","gas_price"]].apply(lambda row: row["gas"] * row["gas_price"], axis=1)
print("\n Total transaction fee: " + str(sai_txs["transaction_fee"].sum))
print("\n Mean transaction fee: " + str(sai_txs["transaction_fee"].mean()))
print("\n Maximum transaction fee:" + str(sai_txs["transaction_fee"].max()))
