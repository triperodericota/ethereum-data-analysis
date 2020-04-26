from django.urls import path, re_path

from . import views

app_name = 'ethereum_analysis_app'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^exchange_rates$', views.exchange_rates_for_country, name='exchange_rates_for_country')
]
