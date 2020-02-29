#!/usr/bin/python3
import pandas as pd
import numpy as np
from datetime import date,timedelta

def daterange(date1, date2):
	for n in range(int ((date2 - date1).days)+1):
		yield date1 + timedelta(n)

def load_dimension(connection_db):
	dates = {'date': [], 'day': [],'month': [], 'year': []}
	start_dt = date(2015,1,1)
	end_dt = date(2020,12,31)
	for dt in daterange(start_dt, end_dt):
		str_date = dt.strftime("%Y-%m-%d")
		#print(str_date)
		dates['date'].append(dt)
		dates['day'].append(dt.day)
		dates['month'].append(dt.month)
		dates['year'].append(dt.year)

	dates = pd.DataFrame(dates)
	dates.to_sql("date_dimension", connection_db,if_exists='append',index=False)
