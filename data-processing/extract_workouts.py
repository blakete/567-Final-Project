import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import xmltodict

# import uncleaned workout data
raw_workouts = pd.read_csv("./raw-data/workouts.csv")

# drop all uneeded columns
raw_workouts.drop(["Unnamed: 0", "@durationUnit", "@durationUnit", "@totalDistanceUnit", "@totalDistance", "@sourceName", "@sourceVersion", "@device", "@startDate", "@endDate", "MetadataEntry", "WorkoutEvent"], axis=1, inplace=True)

# drop outside date range, change dates to dt obj, change type to our own string
end = datetime.datetime(2021, 3, 23)
start = datetime.datetime(2021, 1, 12)
wTypes = {
    "HKWorkoutActivityTypeRowing": "Row",
    "HKWorkoutActivityTypeWalking": "Walk",
    "HKWorkoutActivityTypeRunning": "Run",
    "HKWorkoutActivityTypeElliptical": "Elliptical",
    "HKWorkoutActivityTypeOther": "Strength",
    "HKWorkoutActivityTypeCycling": "Cycle",
}
for index, row in raw_workouts.iterrows():
    date, duration, calories, wType, = row["@creationDate"], row["@duration"], row["@totalEnergyBurned"], row["@workoutActivityType"]
    # print(date, duration, calories, wType)
    date_time = date.split(" ")[0]+" "+date.split(" ")[1]
    dt_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    # drop outside date range
    if end < dt_obj or dt_obj < start :
        raw_workouts.drop(index, inplace=True)
    else:
        # modify those in range to have our date and type label
        raw_workouts.at[index, "@creationDate"] = dt_obj
        raw_workouts.at[index, "@workoutActivityType"] = wTypes[wType]

# change column headers 
raw_workouts.rename(columns = {'@creationDate' : 'Date', '@duration' : 'Duration', '@totalEnergyBurned': 'Calories', '@workoutActivityType': 'Type'}, inplace = True)

workouts = raw_workouts.copy()
# save processed data
workouts.to_csv("./processed-data/workouts.csv")

# sum calories burned and duration for day
date_dict = {}
for index, row in workouts.iterrows():
    date, duration, calories = row["Date"], row["Duration"], row["Calories"]
    key = str(date.date())
    if key in date_dict:
        sumDur, sumCal = date_dict[key]
        date_dict[key] = (sumDur+duration, sumCal+calories)
    else:
        date_dict[key] = (duration, calories)

dates = []
sumDurations = []
sumCalories = []
for key in date_dict:
    dates.append(key)
    sumDurations.append(date_dict[key][0])
    sumCalories.append(date_dict[key][1])
workoutSums = pd.DataFrame(list(zip(dates, sumDurations, sumCalories)), columns=["Date", "Sum Duration", "Sum Calories"])
workoutSums.to_csv("./processed-data/sum-daily-workouts.csv")


# get workout type calories summations for radar chart
workout_type_dict = {}
total = 0
workouts = []
totalCalories = []
percentCalories = []
for index, row in raw_workouts.iterrows():
    wType, calories = row["Type"], row["Calories"]
    total += calories
    if wType in workout_type_dict:
        workout_type_dict[wType] += calories
    else: 
        workout_type_dict[wType] = calories 

for key in workout_type_dict:
    workouts.append(key)
    totalCalories.append(workout_type_dict[key])
    percentCalories.append(workout_type_dict[key]/total)

print("Workout types, total calories, and percent total calories:")
print("labels: [" + ", ".join(["\""+str(elem)+"\"" for elem in workouts]) + "]")
print("data: [" + ", ".join([str(elem) for elem in totalCalories]) + "]")
print("data: [" + ", ".join([str(elem) for elem in percentCalories]) + "]")
