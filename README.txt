FILES:
randomize_data.py: 
Reads in the taxi data as given. For each file it randomizes the data and spits a chunk of it into a one of 675 new files.
It repeats for each original taxi data file appending the new data to the ranomized files. 

split_day_time.py:
Runs through each file (currently random files) and splits the days and times into two columns. 
It also creates a list of unique days (used for getting the weather data).

weather_data.py:
Prints the first and last day needed. Then I manually change those days to queery for the weather data from each of the five neghorhoods.
The data gets stored in a file called '[location].csv' 

combine_data.py:
Rus through each random file and for each data points looks up the correct weather data. 
Then adds the weather data to the original data frame and writes it to a new file.

distance_matrix.py:
Runs through an additional data folder and gets the mean and stdev of all the distances from one location id to another.
This file generates files that feature_engineering.py relies on.

feature_engineering.py:
Splits given features into day, month, year, hour, minute, second, weekday, distance, and travel time. It also throws out data that is
missing weather or for trips shorter than 1 minute or longer than 3 hours. It then writes these to a new file, and creates a 
manifest for these files. 

add_weather.py:
Add the weather to the files. The manifest can be changed depending on which set of files you want to read in. 
Also writes a manifest for weather data.