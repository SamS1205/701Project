import pandas as pd
import numpy as np
import os
import random
from wwo_hist import retrieve_hist_data

os.chdir("D:\TaxiData\\")

# read manifest and get the file names
days = pd.read_csv(os.path.normpath("_days.txt"), header=None)[0]
print(days.size)
# find first day
days = days.sort_values()
print(days.iloc[0])
# find last day
print(days.iloc[days.size-1])

#get weather data
os.chdir("D:\TaxiData\Weather\\")
frequency = 1
start_date = '01-JAN-2017'
end_date = '31-JUL-2017'
api_key = '6aba5042d2d34d2a81b43619211911'
location_list = ['bronx','brooklyn','manhattan','queens','staten_island']
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)