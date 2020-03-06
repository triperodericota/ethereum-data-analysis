#!/usr/bin/python3

#In this file doing exchange rates data exploration analysis (for someones countries)to know what data ara available
#in data sets from differents sources
#calculate differents statistics over data sets to know the data quality from each one and show average,media,etc(describe)
#visualizate data in matplotlib graphics to see more clearly differences between each data sources
#
# In case that for the same country has differents exchanges rates I choose data from Quandl source because is known from
# where the data is extracted (BOE-Bank of England and FRED - Federal Reserve Economic Data)
#

#Data analysis modules
import pandas as pd
import numpy as np
pd.set_option('display.max.columns', 100)

# data visualization
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
#matplotlib inline

import warnings
warnings.filterwarnings('ignore')
from datetime import datetime,date

# Dict from regions
latin_america = {}#'USD_ARS/BCRA':[], 'USD_ARS/Investing':[], 'USD_BZD/Investing':[], 'USD_BZD/Quandl':[], 'USD_MXN/Investing': [],
#    'USD_MXN/Quandl': [], 'USD_VES': [], 'USD_CRC': [], 'USD_GTQ': [], 'USD_NIO': [] }
east_asia_and_pacific = {}
europe_and_central_asia = {}
middle_east_and_north_africa = {}
north_america = {}
south_asia = {}
sub_saharan_africa = {}

def processing_investing_data(dataset_path,label_data,dict_name, region_dict_label):
    df = pd.read_csv(dataset_path, index_col=0 , parse_dates=["Date"])
    print(label_data + "\n")
    print(df.describe(include=[np.number]))
    dict_name[region_dict_label] = df.Price
    #plt.plot(df.Price,color='blue',label='Investing data')

def processing_quandl_data(dataset_path, label_data,dict_name,region_dict_label):
    df = pd.read_json(dataset_path)
    data_frame_data = {'value': [], 'date': []}
    for exchange in df.loc['data'][0]:
            exchange_value = exchange[1]
            exchange_date = datetime.strptime(exchange[0],"%Y-%m-%d")
            exchange_date = date(exchange_date.year,exchange_date.month,exchange_date.day)
            data_frame_data['value'].append(exchange_value)
            data_frame_data['date'].append(exchange_date)
    df = pd.DataFrame(data_frame_data).set_index('date')
    print(label_data + " \n")
    print(df.describe())
    dict_name[region_dict_label] = df.value
    #plt.plot(df.value,color='red',label='Quandl data')

def plot_data(title):
    plt.legend(loc='upper left')
    plt.title(title)
    plt.show()

## Latin America and Caribbean
#Argentinian peso
#BCRA source
arg_ec = pd.read_json("data_source/exchange_rates/Latin America and Caribbean/argentine_peso_bcra.json",orient="records",convert_dates=["d"]).set_index('d')
print("Argentina's peso BCRA exchange rates: \n")
print(arg_ec.describe(include=[np.number]))
latin_america['USD_ARS/BCRA'] = arg_ec.v
#plt.plot(arg_ec.v,color='red',label='BCRA data')
# Investing.com source
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_ARS.csv", "Argentina's peso Investing exchange rates:",latin_america, 'USD_ARS/Investing')
#plot_data("Argentina exchange rates")
# Conclusion: we can see in plots and pandas dataframe describe for this case (Argentina) that both data source have much similar data

#brazilian real
# Investing.com source
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_BZD.csv","Brazilian's real Investing exchange rates:",latin_america, 'USD_BZD/Investing')
# Quandl.com data source
processing_quandl_data("data_source/exchange_rates/Latin America and Caribbean/brazilian_real.json", "Brazilian's real Quandl exchange rates:",latin_america, 'USD_BZD/Quandl')
#plot_data("Brazil exchange rates")
#Venezuelan bolivar
# Quandl.com data source
processing_quandl_data("data_source/exchange_rates/Latin America and Caribbean/venezuelan_bolivar.json", "Venezuelan's bolivar Quandl exchange retes:",latin_america, 'USD_VES')
#plot_data("Venezuela exchange rates")
#Mexican peso
# Investing.com source
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_MXN.csv","Mexican's peso Investing exchange rates:",latin_america, 'USD_MXN/Investing')
# Quandl.com data source
processing_quandl_data("data_source/exchange_rates/Latin America and Caribbean/mexican_peso.json", "Mexican's peso Quandl exchange rates:",latin_america, 'USD_MXN/Quandl')
#plot_data("Brazil exchange rates")
# same conclusion that Argentinian peso
#Costa Rican Colon
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_CRC.csv","Costa Rica's colon Investing exchange rates:",latin_america, 'USD_CRC')
#Guatemala Quetzal
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_GTQ.csv","Guatemala's quetzal Investing exchange rates:",latin_america, 'USD_GTQ')
#Honduras lempira
#processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_HNL.csv","Honduras's lempira Investing exchange rates:", 'USD_HNL')
#Nicaragua Cordoba oro
processing_investing_data("data_source/exchange_rates/Latin America and Caribbean/USD_NIO.csv","Nicaragua's cordoba oro Investing exchange rates:",latin_america, 'USD_NIO')

latin_america_df = pd.DataFrame(latin_america)
latin_america_df.describe()
latin_america_df.plot(subplots=True, layout=(6,2),figsize=(6,6),sharex=False, title='Latin America and Caribbean')
plt.show()

# Conclusion for datasets of Latin America and Caribbean: we can see that for Argentina and Mexico data from differents sources has very similar values, so in these
# case i choose for USD_ARS/BCRA in Argentina and USD_MXN/Investing for Mexico because Investing has time periods more longer than Quandl (equals i can update data sets)
# for Nicaragua, Costa Rica and Guatemala we can see in plots that data is logical, so i can load this data in database
# for Brazil we can see that USD_BZD/Investing data has outliers, so I choose BZD_USD/Quandl
# in Venezuela we can see that for longer time in data set has the same values. it's doubtful (also considering the situtation for this country in the last years), so
# i'm not going to load this data.

#East Asia and Pacific
# subdivide in two plots for major visualization
#Australian dollar
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_AUD.csv', 'Australian dollar Investing exchange rates', east_asia_and_pacific, 'USD_AUD/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/australian_dollar.json', 'Australian dollar Quandl exchange rates', east_asia_and_pacific, 'USD_AUD/Quandl')
#Chinese yuan
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_CNY.csv', 'Chinese Yuan Renminbi Investing exchange rates',east_asia_and_pacific, 'USD_CNY/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/chinese_yuan.json', 'Chinese Yuan Renminbi Quandl exchange rates', east_asia_and_pacific, 'USD_CNY/Quandl')
#Hong kong dollar
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_HKD.csv', 'Hong Kong Dollar Investing exchange rates', east_asia_and_pacific, 'USD_HKD/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/hong_kong_dollar.json', 'Hong Kong dollar Quandl exchange rates', east_asia_and_pacific, 'USD_HKD/Quandl')
#japanese yen
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_JPY.csv', 'Japan yen Investing exchange rates',east_asia_and_pacific, 'USD_JPY/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/japanese_yen.json', 'Japan yen Quandl exchange rates',east_asia_and_pacific, 'USD_JPY/Quandl')

first_plot_key = ['USD_AUD/Investing', 'USD_AUD/Quandl', 'USD_CNY/Investing', 'USD_CNY/Quandl', 'USD_HKD/Investing', 'USD_HKD/Quandl', 'USD_JPY/Investing', 'USD_JPY/Quandl']
first_plot_dict = {}
for key in first_plot_key:
    first_plot_dict[key] = east_asia_and_pacific[key]

east_asia_and_pacific_df = pd.DataFrame(first_plot_dict)
east_asia_and_pacific_df.describe()
east_asia_and_pacific_df.plot(subplots=True, layout=(6,2),figsize=(6,6),sharex=False, title='East Asia and Pacific')
plt.show()

#New Zelland Dollar
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_NZD.csv', 'New Zealand Dollar Investing exchange rates', east_asia_and_pacific, 'USD_NZD/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/new_zealand_dollar.json', 'New Zealand dollar Quandl exchange rates', east_asia_and_pacific, 'USD_NZD/Quandl')
#Signapore dollar
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_SGD.csv', 'Signapore dollar Investing exchange rates', east_asia_and_pacific, 'USD_SGD/Investing')
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/signapore_dollar.json', 'Signapore dollar Quandl exchange rates', east_asia_and_pacific, 'USD_SGD/Quandl')
#Indonesia Rupiah
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_INR.csv', 'Indonesia rupiah Investing exchange rates',east_asia_and_pacific, 'USD_IDR/Investing')
#Malaysian ringgit
processing_quandl_data('data_source/exchange_rates/East Asia and Pacific/malaysian_ringgit.json', 'Malaysian Ringgit Quandl exchange rates', east_asia_and_pacific, 'USD_MYR/Quandl')
#Mongolia Tugrik
#processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_MNT.csv', 'Mongolia Tugrik Investing exchange rates', 'USD_MNT/Investing')
#Philipine peso
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_PHP.csv', 'Philipine peso Investing exchange rates', east_asia_and_pacific, 'USD_PHP/Investing')
#Solomon Island dollar
processing_investing_data('data_source/exchange_rates/East Asia and Pacific/USD_THB.csv', 'Thailand bath Investing exchange rates', east_asia_and_pacific, 'USD_THB/Investing')

first_plot_key = ['USD_NZD/Investing', 'USD_NZD/Quandl', 'USD_SGD/Investing', 'USD_SGD/Quandl', 'USD_IDR/Investing', 'USD_MYR/Quandl', 'USD_PHP/Investing', 'USD_THB/Investing']
first_plot_dict = {}
for key in first_plot_key:
    first_plot_dict[key] = east_asia_and_pacific[key]


east_asia_and_pacific_df1 = pd.DataFrame(first_plot_dict)
east_asia_and_pacific_sdf1.describe()
east_asia_and_pacific_df1.plot(subplots=True, layout=(6,2),figsize=(6,6),sharex=False, title='East Asia and Pacific')
plt.show()

#Conclusion
# Choosen datasets of East Asia and Pacific:
# USD_AUD/Quandl , USD_CNY/Quandl, USD_JPY/Quandl, USD_HKD/Quandl, USD_NZD/Quandl, USD_SGD/Quandl, USD_IDR/Investing
# USD_MYR/Quandl, USD_PHP/Investing, USD_THB/Investing

#Europe and Central Asia
#Denmark's danish krone
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/danish_krone.json', 'Danish Krone Quandl exchange rates', europe_and_central_asia, 'USD_DKK/Quandl')
#Euro
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/euro.json', 'Euro Quandl exchange rates', europe_and_central_asia, 'USD_EUR/Quandl')
#Norwegian krone
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/norwegian_krone.json', 'Norwegian Krone Quandl exchange rates', europe_and_central_asia, 'USD_NOK/Quandl')
#Pound starling
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/pound_starling.json', 'Pound Starling Quandl exchange rates', europe_and_central_asia, 'USD_GBP/Quandl')
#Russian Ruble
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/russian_ruble.json', 'Russian Ruble Quandl exchange rates', europe_and_central_asia, 'USD_RUB/Quandl')
#Swedish Krona
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/sweish_krone.json', 'Swedish Krone Quandl exchange rates', europe_and_central_asia, 'USD_SEK/Quandl')
#Swiss franc
processing_quandl_data('data_source/exchange_rates/Europe and Central Asia/swiss_franc.json', 'Swiss franc Quandl exchange rates', europe_and_central_asia, 'USD_CHF/Quandl')

#Middle East and North America
