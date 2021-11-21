import pandas as pd
import numpy as np
import os
import random

os.chdir("D:\TaxiData\\")

# read manifest and get the file names
files = pd.read_csv("manifest.txt", header=None)[0]
idxs = [i for i in range(0,100000,148)]
print(idxs[len(idxs)-1])
print(len(idxs))
idxs.append(100000)

# Read files one by one and add them to the list of data frames
for i in range(files.size):
    print("i: " + str(i))
    file = files[i]
    df = pd.read_csv(file)
    df = df.sample(frac=1).reset_index(drop=True)
    for j in range(len(idxs) - 1):
        df_partial = df[idxs[i]:idxs[i+1]]
        if i > 0:
            df_partial.to_csv(os.path.normpath("randomized-" + str(j) + ".csv"), mode='a', header=False)
        else:
            df_partial.to_csv(os.path.normpath("randomized-" + str(j) + ".csv"))

#quickly make a manifest for random data
f = open("_random_manifest.txt", "w")
files = []
for i in range(676):
    files.append("randomized-" + str(i) + ".csv\n")
f.writelines(files)
f.close()