import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('dashboard/day.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
outlier_index = day_df[(day_df['season'] == 1) & (day_df['mnth'] == 12)].index
cleaned_day_df = day_df.drop(outlier_index)

average_rental = cleaned_day_df.groupby('season')['cnt'].mean().reset_index()
average_rental_per_month = cleaned_day_df.groupby(['season', 'mnth'])['cnt'].mean().reset_index()

st.title('Bike Sharing Dataset Analysis✨')
st.subheader('By Undissya Putri Maharani')

# No 1
st.header('Pertanyaan 1: Which season has the most customers? And can you show the trend for each weather?')
plt.figure(figsize=(10, 6))
plt.bar(average_rental['season'], average_rental['cnt'], color=['green', 'purple', 'red', 'blue'])
plt.title('Average Bike Rentals in Every Season')
plt.xticks(average_rental['season'], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.xlabel('Season')
plt.ylabel('Average Bike Rentals')
st.pyplot(plt)

plt.figure(figsize=(12, 8))
plt.title('Trend of Average Bike Rentals per Month for Every Season')
plt.xlabel('Month')
plt.ylabel('Average Bike Rentals')
for season_code, color in zip(range(1, 5), ['green', 'purple', 'red', 'blue']):
    subset = average_rental_per_month[average_rental_per_month['season'] == season_code]
    plt.plot(subset['mnth'], subset['cnt'], color=color)
st.pyplot(plt)

# No 2
st.header('Pertanyaan 2: How does the comparison between the number of casual users and registered users differ between holidays and working days?')
total_casual_holidays = cleaned_day_df[cleaned_day_df['holiday'] == 1]['casual'].sum()
total_registered_holidays = cleaned_day_df[cleaned_day_df['holiday'] == 1]['registered'].sum()
total_casual_workingdays = cleaned_day_df[cleaned_day_df['workingday'] == 1]['casual'].sum()
total_registered_workingdays = cleaned_day_df[cleaned_day_df['workingday'] == 1]['registered'].sum()
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.bar(['Casual Users', 'Registered Users'], [total_casual_holidays, total_registered_holidays], color=['blue', 'green'])
plt.title('Casual Users vs Registered Users during Holidays')

plt.subplot(1, 2, 2)
plt.bar(['Casual Users', 'Registered Users'], [total_casual_workingdays, total_registered_workingdays], color=['blue', 'green'])
plt.title('Casual Users vs Registered Users during Working Days')
st.pyplot(plt)

# No 3
st.header('Pertanyaan 3: Can you visualize the trend of bike rental users over time, considering variations in temperature, humidity, and windspeed on a daily basis?')
plt.figure(figsize=(15, 10))

for i, column in enumerate(['temp', 'hum', 'windspeed'], start=1):
    plt.subplot(3, 1, i)
    sns.lineplot(x=cleaned_day_df['dteday'], y=cleaned_day_df[column], color='blue')
    plt.ylabel(column)
    plt.twinx()
    sns.lineplot(x=cleaned_day_df['dteday'], y=cleaned_day_df['cnt'], color='red')
    plt.ylabel('count')

st.pyplot(plt)