# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressDimension(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=100)
    balance = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'address_dimension'


class CountryDimension(models.Model):
    idcountry_dimension = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=5)
    region = models.CharField(max_length=45)
    currency = models.CharField(max_length=45)
    currency_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'country_dimension'


class DaiTransactions(models.Model):
    dai_transactions_id = models.BigAutoField(primary_key=True)
    hash = models.CharField(unique=True, max_length=255)
    block_number = models.BigIntegerField()
    to_address = models.ForeignKey(AddressDimension, models.DO_NOTHING,related_name='to_address')
    from_address = models.ForeignKey(AddressDimension, models.DO_NOTHING,related_name='from_address')
    value = models.FloatField()
    gas = models.BigIntegerField()
    gas_price = models.BigIntegerField()
    transaction_fee = models.BigIntegerField()
    input = models.TextField()
    block_timestamp = models.BigIntegerField()
    date = models.ForeignKey('DateDimension', models.DO_NOTHING)
    date_0 = models.DateField(db_column='date')  # Field renamed because of name conflict.

    class Meta:
        db_table = 'dai_transactions'


class DateDimension(models.Model):
    date_id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    day = models.BigIntegerField()
    month = models.BigIntegerField()
    year = models.BigIntegerField()

    class Meta:
        db_table = 'date_dimension'


class UsdExchangeRates(models.Model):
    usdexchangerates_id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(CountryDimension, models.DO_NOTHING)
    value = models.FloatField()
    date = models.ForeignKey(DateDimension, models.DO_NOTHING)
    date_0 = models.DateField(db_column='date')  # Field renamed because of name conflict.

    class Meta:
        db_table = 'usd_exchange_rates'
