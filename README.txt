There are four files.

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

add_weather_non_random.py:
Adds the weather data to the data read straight from the original zip file. Also does the splitting of the date-time to day and time.
