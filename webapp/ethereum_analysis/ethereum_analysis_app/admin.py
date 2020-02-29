from django.contrib import admin
from .models import CountryDimension,AddressDimension

# Register your models here.
admin.site.register(CountryDimension)
admin.site.register(AddressDimension)
