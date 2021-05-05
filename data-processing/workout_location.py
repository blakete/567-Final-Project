import pandas as pd

# determine outdoor vs indoor workout count
# indoor if column WorkoutRoute is nan (b/c indoor workouts do not have an associated GPS route recording)

# open processed workout file 
workouts = pd.read_csv("./processed-data/workouts.csv")

indoor = 0
outdoor = 0
for index, row in workouts.iterrows():
    route, duration = row["WorkoutRoute"], row["Duration"]
    if pd.isnull(route):
        indoor += duration
    else:
        outdoor += duration

print("Indoor workouts total duration: "+ str(indoor) + "\nOutdoor workouts total duration: " + str(outdoor)) 