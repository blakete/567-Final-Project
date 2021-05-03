# Author: Blake Edwards
import pandas as pd
import xmltodict

#Reading the file and converting it as a dict. 
print("Converting apple health xml file to csv...")
input_path = './raw-data/apple_health_export/export.xml'
with open(input_path, 'r') as xml_file:
    input_data = xmltodict.parse(xml_file.read())
records_list = input_data['HealthData']['Record']
df_records = pd.DataFrame(records_list)
workouts_list = input_data['HealthData']['Workout']
df_workouts = pd.DataFrame(workouts_list)
df_workouts.to_csv("./raw-data/workouts.csv")

