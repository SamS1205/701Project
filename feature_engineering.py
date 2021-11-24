import pandas as pd
import os
import datetime
import numpy as np

os.chdir("D:\TaxiData\\")

# read in file
files = pd.read_csv(os.path.normpath("manifest.txt"), header=None)[0]

nan_distances = []
dist_means = np.loadtxt("ExtraData\_dist_means.txt")

for i in range(files.size):
    print("i: " + str(i))
    file = os.path.normpath(files[i])
    df = pd.read_csv(file)
    df[['PickupDate', 'PickupTime']] = df.tpep_pickup_datetime.str.split(expand=True)
    df[["PickupYear", "PickupMonth", "PickupDay"]] = df.PickupDate.str.split(pat="-", expand=True)
    df[["PickupHour", "PickupMinute", "PickupSecond"]] = df.PickupTime.str.split(pat=":", expand=True)
    df[['DropoffDate', 'DropoffTime']] = df.tpep_dropoff_datetime.str.split(expand=True)
    df[["DropoffYear", "DropoffMonth", "DropoffDay"]] = df.DropoffDate.str.split(pat="-", expand=True)
    df[["DropoffHour", "DropoffMinute", "DropoffSecond"]] = df.DropoffTime.str.split(pat=":", expand=True)
    df.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    df = df.astype({"PickupYear": "int", "PickupMonth": "int", "PickupDay": "int",
                    "DropoffYear": "int", "DropoffMonth": "int", "DropoffDay": "int",
                    "PickupHour": "int", "PickupMinute": "int", "PickupSecond": "int",
                    "DropoffHour": "int", "DropoffMinute": "int", "DropoffSecond": "int"})
    df["PickupDayOfWeek", "DropoffDayOfWeek", "TravelTime"] = None
    #print(df.dtypes)
    drop_idx = []
    for index, row in df.iterrows():
        if index % 1000 == 0:
            print("i: " + str(i) + ", index: " + str(index))

        # Get the distance from the location IDs
        d_row = row["PULocationID"] - 1
        d_col = row["DOLocationID"] - 1
        df.loc[index, "TravelTime"] = dist_means[d_row][d_col]
        if dist_means[d_row][d_col] == np.nan:
            nan_distances.append((i, index))
            print("Nan Distance at file: "+str(i)+", index: "+str(index))

        # Get the day of the week
        pickup_date = datetime.datetime(row["PickupYear"], row["PickupMonth"], row["PickupDay"])
        df.loc[index, "DropoffDayOfWeek"] = pickup_date.weekday()
        dropoff_date = datetime.datetime(row["DropoffYear"], row["DropoffMonth"], row["DropoffDay"])
        df.loc[index, "DropoffDayOfWeek"] = dropoff_date.weekday()

        # Get travel time
        pickup_time = datetime.datetime(row["PickupYear"], row["PickupMonth"], row["PickupDay"], row["PickupHour"],
                                        row["PickupMinute"], row["PickupSecond"])
        dropoff_time = datetime.datetime(row["DropoffYear"], row["DropoffMonth"], row["DropoffDay"], row["DropoffHour"],
                                        row["DropoffMinute"], row["DropoffSecond"])
        time = dropoff_time - pickup_time
        df.loc[index, "TravelTime"] = time.seconds/60

        #print("Index is: " + str(index) + ". DF size is: " + str(df.size))
        # delete row if the travel time is less than 1 minute and greater than 6 hours
        if time.seconds/60 < 1 or time.seconds/60/60 > 6:
            drop_idx.append(index)
        # delete row if the pick up or drop off year is < 2008
        elif df.iloc[index]["PickupYear"] < 2008 or df.iloc[index]["DropoffYear"] < 2008:
            drop_idx.append(index)
            #df = df.drop(index=index, inplace=True)
    for idx in drop_idx:
        df = df.drop(index=idx)
    # Write the new df to a new file
    df.to_csv(os.path.normpath("data-engineered-features-" + str(i) + ".csv"))
#quickly make a manifest for random data
f = open("_engineered_feature_manifest.txt", "w")
files = []
for i in range(files.size):
    files.append("data-engineered-features-" + str(i) + ".csv\n")
f.writelines(files)
f.close()

# print out file with nan distances
print(nan_distances)