import pandas as pd
import datetime

workouts = pd.read_csv("./processed-data/sum-daily-workouts.csv")
logged_symptoms = pd.read_csv("./processed-data/avg-daily-anxiety.csv")

# generate list of dates between 01/12/21 - 03/23/21
start = datetime.datetime(2021, 1, 12)
end = datetime.datetime(2021, 3, 23)
currDate = start
dates = []
durations = []
calories = []
symptoms = []
while currDate <= end:
    dates.append(str(currDate.date()))
    durations.append(0)
    calories.append(0)
    symptoms.append("null")
    currDate = currDate + datetime.timedelta(days=1)

for index, row in workouts.iterrows():
    date, sumDuration, sumCalories = row["Date"], row["Sum Duration"], row["Sum Calories"]
    idx = dates.index(str(date))
    durations[idx] = sumDuration
    calories[idx] = sumCalories

for index, row in logged_symptoms.iterrows():
    date, anxiety = row["Date"], row["Anxiety"]
    idx = dates.index(date)
    symptoms[idx] = anxiety

joined_data = pd.DataFrame(list(zip(dates, durations, calories, symptoms)), columns=["Date", "Duration", "Calories", "Symptoms"])
joined_data.to_csv("./processed-data/joined.csv")

# export to format that we can plot
print("labels: " + "[" + ', '.join(["\""+str(elem)+"\"" for elem in dates]) + "]")
print("\ndata: " + "[" + ', '.join([str(elem) for elem in durations]) + "]")
print("\ndata: " + "[" + ', '.join([str(elem) for elem in calories]) + "]")
print("\ndata: " + "[" + ', '.join([str(elem) for elem in symptoms]) + "]")