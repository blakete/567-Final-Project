import time
import json
import datetime
import pandas as pd

# get workout times of day 
# output as json array in format

# open processed workout file 
workouts = pd.read_csv("./processed-data/workouts.csv")
# find all unique workout types
workout_types = {"All": 1}
for index, row in workouts.iterrows():
    workout_type = row["Type"]
    if workout_type not in workout_types:
        workout_types[workout_type] = 1
# create datastructure to hold heatmap points for all workout types
workout_heatmap = {}
for wt in workout_types:
    for i in range(1,8):
        for j in range(1,24,2):
            key = (wt,i,j)
            workout_heatmap[key] = 0

# iterate workouts and increment corresponding workout_heatmap key based on type, weekday, and hour
for index, row in workouts.iterrows():
    wt, date = row["Type"], row["Date"]
    dt_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    x = (dt_obj.isoweekday() % 7) + 1
    y = dt_obj.hour + (not (dt_obj.hour%2))
    key = (wt,x,y)
    workout_heatmap[key] += 1
    workout_heatmap[('All',x,y)] += 1

# for key in workout_heatmap:
#     print(key, workout_heatmap[key])

# convert workout heatmap dictionary to plotable json object
backgroundColors = ["rgb(54, 162, 235)", "rgb(255, 99, 132)","rgb(75, 192, 192)","rgb(245, 230, 66)","rgb(201, 203, 207)","rgb(245, 167, 66)","rgb(54, 162, 235)"]
datasets = []
# workout_types = {"All": 1} # for testing
for wt in workout_types:
    dataset = {
        "label": wt,
        "backgroundColor": backgroundColors.pop(0) # NOTE: assumes we only have 5 workout types, will need to change if want to support more
    }
    data = []
    for i in range(1,8):
        for j in range(1,24,2):
            key = (wt,i,j)
            pt = {
                "x": i,
                "y": j,
                "r": workout_heatmap[key]
            }
            data.append(pt)
    dataset["data"] = data
    datasets.append(dataset)

print(json.dumps(datasets))

total = 0
for key in workout_heatmap:
    wt, x, y = key
    if wt == "All":
        total += workout_heatmap[key]
print(total)