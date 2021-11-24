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
print(days)
with open("_days.txt", 'w') as f:
    f.writelines(["%s\n" % item  for item in list(days)])
f.close()

#get weather data
os.chdir("D:\TaxiData\Weather\\2016\\")
frequency = 1
start_date = '10-DEC-2016'
end_date = '10-DEC-2016'
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
os.chdir("D:\TaxiData\Weather\\2017\\")
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

os.chdir("D:\TaxiData\Weather\\2008\\")
frequency = 1
start_date = '31-DEC-2008'
end_date = '31-DEC-2008'
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
os.chdir("D:\TaxiData\Weather\\2009\\")
frequency = 1
start_date = '01-JAN-2009'
end_date = '02-JAN-2009'
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

# data not available for these dates
#start_date = '22-JUL-1997'
#end_date = '22-JUL-1997'
#start_date = '01-JAN-2001'
#end_date = '06-JAN-2001'
#start_date = '31-DEC-2002'
#end_date = '31-DEC-2002'
#start_date = '01-JAN-2003'
#end_date = '14-JAN-2003'

#combine weather data
os.chdir("D:\TaxiData\Weather\\")

years = ["2017", "2016", "2008", "2009"]
# for each year
for year in years:
    #get data for that year and append it to the main file
    for loc in location_list:
        bronx_df = pd.read_csv(os.path.normpath(year + "\\" + loc + ".csv"))
        if year == "2017":
            bronx_df.to_csv(os.path.normpath(loc + ".csv"), index=False)
        else:
            bronx_df.to_csv(os.path.normpath(loc + ".csv"), mode='a', header=False, index=False)
