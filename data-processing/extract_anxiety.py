# Author: Blake Edwards
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# get symptom date range to parse workouts csv 

# PARSE perceived-symptoms.csv
# load csv
ps_df = pd.read_csv("./raw-data/export.csv")
# get the date, period, anxiety columns
anxiety_df = ps_df[["Date", "Period", "Anxiety"]].copy()

# how many and on what days did i log anxiety < 3 times
# date_dict = {}
# for index, row in anxiety_df.iterrows():
#     date, period, value = row["Date"], row["Period"], row["Anxiety"]
#     if pd.isnull(value):
#         if date in date_dict:
#             date_dict[date] += 1
#         else:
#             date_dict[date] = 1
#     # print(date, period, pd.isnull(value))
# for index in date_dict:
#     if date_dict[index] > 1:
#         print(index, date_dict[index])
# result: get 01/12/21 - 03/23/21

# convert date string and period string to one datetime
period_delta = {
    "am": datetime.timedelta(seconds=25200),
    "mid": datetime.timedelta(seconds=43200),
    "pm": datetime.timedelta(seconds=61200),
    "nite": datetime.timedelta(seconds=79200),
}
for index,row in anxiety_df.iterrows():
    date, period, value = row["Date"], row["Period"], row["Anxiety"]
    year, month, day = date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    dt = datetime.datetime(year, month, day)
    # save datetime, adjusting for period
    anxiety_df.at[index, "Date"] = dt + period_delta[period]
anxiety_df.drop("Period", axis=1, inplace=True)


# drop all rows outside of 01/12/21 - 03/23/21
print("size before: ", anxiety_df.shape)
end = datetime.datetime(2021, 3, 24)
start = datetime.datetime(2021, 1, 12)
for index, row in anxiety_df.iterrows():
    date, value = row["Date"], row["Anxiety"]
    if end < date or date <= start :
        anxiety_df.drop(index, inplace=True)
print("size after: ", anxiety_df.shape)

# how many and what days have < 3 logs?
# drop days with < 3 logs
print("size before: ", anxiety_df.shape)
total = 0
date_dict = {}
for index, row in anxiety_df.iterrows():
    date, value = row["Date"], row["Anxiety"]
    key = str(date.date())
    if key not in date_dict:
        date_dict[key] = 0
    if pd.isnull(value):
        date_dict[key] += 1
# remove < 3 log dates from anxiety dataframe
for index, row in anxiety_df.iterrows():
    date = row["Date"]
    key = str(date.date())
    if key in date_dict:
        if date_dict[key] > 2:
            total += 1
            anxiety_df.drop(index, inplace=True)
            
print("Total dropped days: ", total/4) # 4 records per day
print("size after: ", anxiety_df.shape)

# result: 4 days in this range have < 3 logs

# save anxiety annotations to clean CSV
anxiety_df.to_csv("./processed-data/anxiety.csv")

# create CSV with average anxiety score for each day
date_dict = {}
for index, row in anxiety_df.iterrows():
    date, value = row["Date"], row["Anxiety"]
    key = str(date.date())
    if not pd.isnull(value):
        # save or update (running_total, count)
        if key in date_dict:
            curr_ttl, cnt = date_dict[key]
            date_dict[key] = (curr_ttl+value, cnt+1)
        else:
            date_dict[key] = (value, 1)

date = []
avg = []
for key in date_dict:
    total, cnt = date_dict[key]
    curr_avg = total / cnt
    date.append(datetime.datetime(int(key.split("-")[0]), int(key.split("-")[1]), int(key.split("-")[2])))
    avg.append(curr_avg)

# save average daily anxiety to clean CSV
avg_anxiety = pd.DataFrame(list(zip(date, avg)), columns=["Date", "Anxiety"])
avg_anxiety.to_csv("./processed-data/avg-daily-anxiety.csv")


