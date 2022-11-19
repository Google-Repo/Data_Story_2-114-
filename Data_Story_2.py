#all modules will be imported here:
import csv
import statistics
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

#plotly graph:
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df,y = "quant_saved", color = 'highschool_completed')
fig.show()

#Calculation Mean, Median and Mode:
print('Mean and Median for the data:')
with open("savings_data_final.csv",newline= '') as f:
    reader = csv.reader(f)
    savings_data = list(reader)


#Calculating Interquatile range:
q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1

print(f"Q1 - {q1}")
print(f"Q3 - {q3}")
print(f"IQR - {iqr}")

lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr

#Creating a new Dataframe:
new_df = df[df["quant_saved"] < upper_whisker]

all_savings = []
all_savings = new_df["quant_saved"].tolist()

print(f"Mean of Savings - {statistics.mean(all_savings)}")
print(f"Median of Savings - {statistics.median(all_savings)}")
print(f"Mode of Savings - {statistics.mode(all_savings)}")
print(f"Standard Deviation in savings - {statistics.stdev(all_savings)}")

fig = ff.create_distplot([new_df["quant_saved"].tolist()], ["Savings"], show_hist = False)
fig.show()

#Collecting 1000 samples of 100 data points each, savings their averages in a list

sampling_mean_list = []
for i in range(100):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(all_savings))
    sampling_mean_list.append(statistics.mean(temp_list))

mean_sampling = statistics.mean(sampling_mean_list)

fig = ff.create_distplot([sampling_mean_list], ["Savings(Sampling)"], show_hist = False)
fig.add_trace(go.Scatter(x= [mean_sampling,mean_sampling], y= [0, 0.1], mode = "lines", name="MEAN"))
fig.show()

print(f"Standard deviation of the Sampling Data - {statistics.stdev(sampling_mean_list)}")

print(f"Mean of Population - {statistics.stdev(sampling_mean_list)}")
print(f"Mean of Sampling Distribution - {mean_sampling}")

#temp_df will have the rows where age is not 0 
temp_df = new_df[new_df.age != 0]

age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")

reminded_df = new_df.loc[new_df["rem_any"] == 1]
not_reminded_df = new_df.loc[new_df["rem_any"] == 0]

print(reminded_df.head())
print(not_reminded_df.head())

fig = ff.create_distplot([not_reminded_df["quant_saved"].tolist()] , ["Savings (Not Reminded)"], show_hist = False)
fig.show()

not_reminded_savings = not_reminded_df["quant_saved"].tolist()

sampling_mean_list_not_reminded = []
for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(not_reminded_savings))
    sampling_mean_list_not_reminded.append(statistics.mean(temp_list))

mean_sampling_not_reminded = statistics.mean(sampling_mean_list_not_reminded)
stdev_sampling_not_reminded = statistics.stdev(sampling_mean_list_not_reminded)

print(f"Mean of Sampling (Not Reminded) -> {mean_sampling_not_reminded}")
print(f"Standard Deviation of Sampling (Not Reminded) -> {stdev_sampling_not_reminded}")

fig = ff.create_distplot([sampling_mean_list_not_reminded], ["Savings (Sampling)"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling, mean_sampling], y=[0,0.1], mode= "lines", name= "MEAN"))
fig.show()

first_std_deviation_start = mean_sampling_not_reminded-stdev_sampling_not_reminded
first_std_deviation_end = mean_sampling_not_reminded+stdev_sampling_not_reminded
print(f"First (start) - {first_std_deviation_start} and First (end) - {first_std_deviation_end}")

second_std_deviation_start = mean_sampling_not_reminded-(2*stdev_sampling_not_reminded)
second_std_deviation_end = mean_sampling_not_reminded+(2*stdev_sampling_not_reminded)
print(f"Second (start) - {second_std_deviation_start} and Second (end) - {second_std_deviation_end}")

third_std_deviation_start = mean_sampling_not_reminded-(3*stdev_sampling_not_reminded)
third_std_deviation_end = mean_sampling_not_reminded+(3*stdev_sampling_not_reminded)
print(f"Third (start) - {third_std_deviation_start} and Third (end) - {third_std_deviation_end}")

reminded_savings = reminded_df["quant_saved"].tolist()

sampling_mean_list_reminded = []
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(reminded_savings))
  sampling_mean_list_reminded.append(statistics.mean(temp_list))

mean_sampling_reminded = statistics.mean(sampling_mean_list_reminded)
stdev_sampling_reminded = statistics.stdev(sampling_mean_list_reminded)

print(f"Mean of Sampling (Reminded) -> {mean_sampling_reminded}")
print(f"Standard Deviation of Sampling (Reminded) -> {stdev_sampling_reminded}")
fig = ff.create_distplot([sampling_mean_list_reminded], ["Savings (Sampling)"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling, mean_sampling], y=[0, 0.1], mode="lines", name="MEAN"))
fig.show()


z_score = (mean_sampling_reminded - mean_sampling_not_reminded) / stdev_sampling_not_reminded
print(f"Z-Score is - {z_score}")

