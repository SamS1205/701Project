import pandas as pd
import os

os.chdir("D:\TaxiData\\")

# read in files
# CHANGE THE MANIFEST NAME DEPENDING ON WHAT DATA YOU WANT TO READ IN
files = pd.read_csv(os.path.normpath("manifest.txt"), header=None)[0]

zones = pd.read_csv(os.path.normpath("taxi _zone_lookup.csv"))
bronx_zones = zones.loc[zones["Borough"] == "Bronx"]["LocationID"].to_numpy()
brooklyn_zones = zones.loc[zones["Borough"] == "Brooklyn"]["LocationID"].to_numpy()
manhattan_zones = zones.loc[zones["Borough"] == "Manhattan"]["LocationID"].to_numpy()
queens_zones = zones.loc[zones["Borough"] == "Queens"]["LocationID"].to_numpy()
bronstaten_island_zones = zones.loc[zones["Borough"] == "Staten Island"]["LocationID"].to_numpy()

bronx_weather = pd.read_csv(os.path.normpath("Weather\\bronx.csv"))
brooklyn_weather = pd.read_csv(os.path.normpath("Weather\\brooklyn.csv"))
manhattan_weather = pd.read_csv(os.path.normpath("Weather\\manhattan.csv"))
queens_weather = pd.read_csv(os.path.normpath("Weather\\queens.csv"))
staten_island_weather = pd.read_csv(os.path.normpath("Weather\\staten_island.csv"))

weather_conds = ["maxtempC","mintempC","totalSnow_cm","sunHour","uvIndex","moon_illumination","moonrise","moonset",
                 "sunrise","sunset","DewPointC","FeelsLikeC","HeatIndexC","WindChillC","WindGustKmph","cloudcover",
                 "humidity","precipMM","pressure","tempC","visibility","winddirDegree","windspeedKmph"]

print(queens_weather.iloc[[0]][weather_conds])

for i in range(files.size):
    print("i: " + str(i))
    file = os.path.normpath(files[i])
    df = pd.read_csv(file)
    df[['PickupDate', 'PickupTime']] = df.tpep_pickup_datetime.str.split(expand=True)
    df[['DropoffDate', 'DropoffTime']] = df.tpep_dropoff_datetime.str.split(expand=True)
    df.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    weather = pd.DataFrame(columns=weather_conds)
    for index, row in df.iterrows():
        if index % 1000 == 0:
            print("i: " + str(i) + ", index: " + str(index))
        loc_id = row["PULocationID"]
        day = row["PickupDate"]
        time = row["PickupTime"]
        datetime = day + " " + time[0:2]+":00:00"
        #find the weather data for the given location
        if loc_id in bronx_zones:
            idx = bronx_weather.index[bronx_weather["date_time"] == datetime]
            weather_data = bronx_weather.iloc[[idx[0]]][weather_conds]
        if loc_id in brooklyn_zones:
            idx = brooklyn_weather.index[brooklyn_weather["date_time"] == datetime]
            weather_data = brooklyn_weather.iloc[[idx[0]]][weather_conds]
        if loc_id in manhattan_zones:
            idx = manhattan_weather.index[manhattan_weather["date_time"] == datetime]
            weather_data = manhattan_weather.iloc[[idx[0]]][weather_conds]
        if loc_id in queens_zones:
            idx = queens_weather.index[queens_weather["date_time"] == datetime]
            print(idx)
            print(queens_weather.iloc[[idx[0]]][weather_conds])
            weather_data = queens_weather.iloc[[idx[0]]][weather_conds]
        weather = pd.concat((weather, weather_data), ignore_index=True)
    df[weather_conds] = weather[weather_conds]
    df.to_csv(os.path.normpath("weather-" + str(i) + ".csv"))
    print(df)
f = open("_weather_manifest.txt", "w")
files = []
for i in range(files.size):
    files.append("weather-" + str(i) + ".csv\n")
f.writelines(files)
f.close()