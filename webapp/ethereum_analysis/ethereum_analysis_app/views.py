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
#from bokeh.models.callbacks import CustomJS
import datetime
import pdb

def index(request):

    #countries_ids_with_exchanges = []
    countries_with_exchanges = UsdExchangeRates.objects.order_by('country').distinct('country')
    #for country in countries_with_exchanges:
    #    countries_ids_with_exchanges.append(country.)
    #query = 'select * from country_dimension where idcountry_dimension in %s'
    #countries_with_exchanges = CountryDimension.objects.raw(query, params=[tuple(countries_ids_with_exchanges)])

    dai_transactions = DaiTransactions.objects.all()
    dai_transactions_df = read_frame(dai_transactions).set_index('dai_transactions_id')
    group_by_dates = dai_transactions_df.groupby('date_0')
    amount_of_txs_per_day = group_by_dates.size().to_frame()
    amount_of_txs_per_day = amount_of_txs_per_day.rename(columns={0:'count'})
    source = ColumnDataSource.from_df(amount_of_txs_per_day)

    plot = figure(title="DAI's transactions", y_axis_label= "Transaction's count", plot_width=1000, plot_height=500)
    l=plot.line(x='date_0',y='count', legend= "DAI's transactions", line_width=2, source=source)
    plot.xaxis.formatter = DatetimeTickFormatter(days=["%d %m %Y"])

    # adding hover interaction to plot
    hover = HoverTool(tooltips=[('date',"@date_0{%Y-%m-%d}"),('count','@count')],formatters={'date_0':'datetime'})
    plot.add_tools(hover)

    script, div = components(plot)
    #pdb.set_trace()
    return render(request,'ethereum_analysis_app/index.html',{'script': script, 'div': div, 'exchanges_rates': list(countries_with_exchanges)})


def exchange_rates_for_country(request):
    print(request)
    # start and end dates for not retrieve all exchanges rates
    start_date = datetime.date(2019,11,23)
    end_date = datetime.date(2019,12,13)

    country_selected = request.GET.get("country_select")
    print(country_selected)
    country_selected = CountryDimension.objects.filter(name=country_selected).first()
    exchange_rates = UsdExchangeRates.objects.filter(Q(country=country_selected) & Q(date_0__range=(start_date,end_date)))
    exchange_rates_df = read_frame(exchange_rates).set_index('date_0')

    title = "USD/" + country_selected.currency_code + " Exchange rates"
    exchange_rates_plot = figure(title=title, y_axis_label=country_selected.currency, plot_width=1000, plot_height=500)
    exchange_rates_plot.line(exchange_rates_df.index, exchange_rates_df.value, legend=country_selected.currency, line_width=2)
    exchange_rates_plot.xaxis.formatter = DatetimeTickFormatter(days=["%d %m %Y"])

    er_script, er_div = components(exchange_rates_plot)
    return JsonResponse({'er_script': er_script, 'er_div': er_div})
