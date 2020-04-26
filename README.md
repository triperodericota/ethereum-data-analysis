# ethereum-data-analysis

Ethereum Data Analysis is a project framed in Business Intelligence area, where I made an analysis over some DAI's (currently SAI) stablecoin transactions on the Ethereum blockchain and join data with dollar's exchanges rates from differents currencies to know if some of this affect to DAI's transactions and values. I designed a Data Warehouse following the Kimball principles and load this from an ETL process using Pandas library and open data sets, then all data is processed and reported on a web portal.

You can use the app on https://daitransactionsanalysis.herokuapp.com/app. Here, you can view the DAI's transactions in the period between 24-11-2019 and 10-12-2019, the transactions's count, the mount for transactions in DAI's value(only some of these contain a mount value)  and a mount in USD (it's said that 1 DAI = 1 USD). If you select a country/currency you will seeign the curve that represent the currency's cotization to dollar respctc, and the mount of DAI's transactions in this currency.

**Project's structure**


**ETL**


In ETL folder, you can find all scripts used to Extract data from open data sources, make the data exploration using Panda's functions and plotting, Transform some of this data and Load this on a Data Wareahouse.

The dollar's exchange rates data sources, come form Investing portal (https://www.investing.com/currencies/) and Quandl API (https://blog.quandl.com/api-for-currency-data). In case for differencies between such datasets, in general was choosen data from Quandl's because the source from which they come is known(BOE-Bank of England, FRED - Federal Reserve Economic Data, etc).  You can run ETL/data_exploration.py to know general stadistics and properties for this data sets

The data for the Ethereum blockchain, specifically DAI's block were extracted using Ethereum ETL (https://github.com/blockchain-etl/ethereum-etl#export_blocks_and_transactions). You can run ETL/blockchain_data_exploration.py to know general stadistics and properties for blocks used to load the Data Warehouse.

ETL/main_job.py is the file that invokes to all transformations that create and load the database's tables.


**Webapp**

In webapp folder, you can see the code for the Django's project that contain an app used to read data loaded during the ETL process, handler this using Pandas's DataFrame funtions and reporting this on HTML page using Bokeh (https://docs.bokeh.org/en/latest/docs/dev_guide.html) library.
