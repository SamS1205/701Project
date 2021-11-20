import pandas as pd
import numpy as np
import os
import random
import json

os.chdir("D:\TaxiData\\")

# read manifest and get the file names
files = pd.read_csv(os.path.normpath("random_manifest.txt"), header=None)[0]

# Read files one by one and split the day and time into two columns for both pickup and drop off
# also put the day into a set
days = set()
for i in range(files.size):
    print("i: " + str(i))
    file = os.path.normpath(files[i])
    df = pd.read_csv(file)
    df[['PickupDate', 'PickupTime']] = df.tpep_pickup_datetime.str.split(expand=True)
    df[['DropoffDate', 'DropoffTime']] = df.tpep_dropoff_datetime.str.split(expand=True)
    df.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    days.update(df.PickupDate.unique())
    days.update(df.DropoffDate.unique())
    df.to_csv(file)
print(days)
with open("_days.txt", 'w') as f:
    f.writelines(["%s\n" % item  for item in list(days)])
f.close()