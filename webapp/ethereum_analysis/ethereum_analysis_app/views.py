from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django_pandas.io import read_frame
from .models import *
from django.db import connection
from django.db.models import Q
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource,CustomJS,HoverTool
from bokeh.embed import components
from bokeh.models.formatters import DatetimeTickFormatter
import datetime
import time
import pdb
import pandas as pd

def retrieve_eth_usd_in(range_of_timestamps):
    source = pd.read_json("../../ETL/data_source/exchange_rates/eth_to_usd.json")
    exchanges = source['Data']['Data']
    data_frame_data = {'date':[], 'value':[]}
    for elem in exchanges:
        if(elem['time'] in range_of_timestamps):
            data_frame_data['date'].append(datetime.datetime.fromtimestamp(elem['time']))
            data_frame_data['value'].append(elem['close'])
        elif(elem['time'] > range_of_timestamps[len(range_of_timestamps) - 1]):
            break

    return pd.DataFrame(data_frame_data).set_index('date')

def calculate_txs_amount_in_usd(df_txs, df_exchanges):
    #convert wei value to ether (1 wei = 1000000000000000000 ether)
    df_txs['value_in_ether'] = [((value * 1000000000000000000) / 1) for value in df_txs['amount']]
    #df_txs[to_usd] = df_exchanges[df_exchanges.date == txs.date]['value'] * txs['value_in_ether'] for txs in df_t
    usd_values = []
    for txs in df_txs.itertuples():
        usd_values.append(df_exchanges[df_exchanges.index.date == txs[0]]['value'] * txs[3])
    df_txs['value_to_usd'] = [elem[0] for elem in usd_values]

def index(request):

    countries_with_exchanges = UsdExchangeRates.objects.order_by('country').distinct('country').values('country')
    countries_with_exchanges = CountryDimension.objects.filter(idcountry_dimension__in=countries_with_exchanges)
    countries_with_exchanges_df = read_frame(countries_with_exchanges)
    group_by_region = countries_with_exchanges_df.groupby('region')
    #for country in countries_with_exchanges:
    #    countries_ids_with_exchanges.append(country.)
    #query = 'select * from country_dimension where idcountry_dimension in %s'
    #countries_with_exchanges = CountryDimension.objects.raw(query, params=[tuple(countries_ids_with_exchanges)])

    dai_transactions = DaiTransactions.objects.all()
    dai_transactions_df = read_frame(dai_transactions).set_index('dai_transactions_id')
    group_by_dates = dai_transactions_df.groupby('date_0')
    txs_per_day = group_by_dates.size().to_frame()
    txs_per_day = txs_per_day.rename(columns={0:'count'})
    txs_per_day["amount"] = group_by_dates.sum()['value']

    #retrieve exchanges ETH/USD
    eth_to_usd = retrieve_eth_usd_in(list(time.mktime(txs_date.timetuple()) for txs_date in txs_per_day.index))
    calculate_txs_amount_in_usd(txs_per_day, eth_to_usd)
    source = ColumnDataSource.from_df(txs_per_day)

    plot = figure(title="DAI's transactions", y_axis_label= "Transaction's count", plot_width=1000, plot_height=500)
    l=plot.line(x='date_0',y='count', legend= "DAI's transactions", line_width=2, source=source)
    plot.xaxis.formatter = DatetimeTickFormatter(days=["%d %m %Y"])

    # adding hover interaction to plot
    hover = HoverTool(tooltips=[('date',"@date_0{%Y-%m-%d}"),('count','@count'),('amount','@amount'),('amount in usd','@value_to_usd')],formatters={'date_0':'datetime'})
    plot.add_tools(hover)
    
    script, div = components(plot)
    return render(request,'ethereum_analysis_app/index.html',{'script': script, 'div': div, 'countries_by_region': group_by_region})


def exchange_rates_for_country(request):
    # start and end dates for not retrieve all exchanges rates
    start_date = datetime.date(2019,11,23)
    end_date = datetime.date(2019,12,13)

    country_selected = request.GET.get("country_select")
    country_selected = CountryDimension.objects.filter(name=country_selected).first()
    exchange_rates = UsdExchangeRates.objects.filter(Q(country=country_selected) & Q(date_0__range=(start_date,end_date)))
    exchange_rates_df = read_frame(exchange_rates).set_index('date_0')

    title = "USD/" + country_selected.currency_code + " Exchange rates"
    exchange_rates_plot = figure(title=title, y_axis_label=country_selected.currency, plot_width=1000, plot_height=500)
    exchange_rates_plot.line(exchange_rates_df.index, exchange_rates_df.value, legend=country_selected.currency, line_width=2)
    exchange_rates_plot.xaxis.formatter = DatetimeTickFormatter(days=["%d %m %Y"])

    er_script, er_div = components(exchange_rates_plot)
    return JsonResponse({'er_script': er_script, 'er_div': er_div})
