import pandas as pd

# determine outdoor vs indoor workout count
# indoor if column WorkoutRoute is nan (b/c indoor workouts do not have an associated GPS route recording)

# open processed workout file 
workouts = pd.read_csv("./processed-data/workouts.csv")

indoor = 0
outdoor = 0
for index, row in workouts.iterrows():
    route = row["WorkoutRoute"]
    if pd.isnull(route):
        indoor += 1
    else:
        outdoor += 1

print("Indoor workouts: "+ str(indoor) + "\nOutdoor workouts: " + str(outdoor)) 