import numpy as np
import pandas as pd
import os

os.chdir("D:\TaxiData\ExtraData\\")

# file names
files = ["green_tripdata_2018-02", "green_tripdata_2018-04", "green_tripdata_2018-06",
         "green_tripdata_2018-08", "green_tripdata_2018-10", "green_tripdata_2018-12",
         "yellow_tripdata_2018-01", "yellow_tripdata_2018-03", "yellow_tripdata_2018-05",
         "yellow_tripdata_2018-07", "yellow_tripdata_2018-09", "yellow_tripdata_2018-11",
         "yellow_tripdata_2017-01", "yellow_tripdata_2017-02", "yellow_tripdata_2017-03",
         "yellow_tripdata_2017-04", "yellow_tripdata_2017-05", "yellow_tripdata_2017-06",
         "yellow_tripdata_2017-07"]

#initialize distance matrix as 2d array of 263x263 with each of those elements being a list
dists = np.empty((265,265), dtype=np.ndarray)
for i in range(265):
    for j in range(265):
        dists[i][j] = []

# go through each file and read in the data
for i in range(len(files)):
#for i in range(1):
    print("i: " + str(i))
    file = os.path.normpath(files[i]+".csv")
    df = pd.read_csv(file)

    df = df.astype({"PULocationID": "int", "DOLocationID": "int", "trip_distance": "float"})

    # for each row in the dataframe
    for index, row in df.iterrows():
        if index % 10000 == 0:
            print("i: " + str(i) + ", index: " + str(index))
        # add the distance to the list at [pickup ID][dropoff ID]
        d_row = row["PULocationID"]-1
        d_col = row["DOLocationID"]-1
        l = dists[d_row][d_col]
        l.append(row["trip_distance"])
        dists[d_row][d_col] = l
#write array to file
#dists.savetxt("_dist_matrix.txt")
for i in range(265):
    for j in range(265):
        if (len(dists[i][j]) == 0):
            print("empty for ("+str(i)+", "+str(j)+")")
        np.savetxt("Dists\\row-"+str(i)+"-col-"+str(j)+".csv", dists[i][j])
dist_mean = np.zeros((265, 265))
dist_stdev = np.zeros((265, 265))
#np.savetxt("_dist_matrix.txt", dists)
for i in range(265):
    print(i)
    for j in range(265):
        dist_mean[i][j] = np.average(dists[i][j])


        dist_stdev[i][j] = np.std(dists[i][j])
np.savetxt("_dist_means.txt", dist_mean)
np.savetxt("_dist_stdevs.txt", dist_stdev)
#np.savetxt("_dist_matrix.txt", dists)