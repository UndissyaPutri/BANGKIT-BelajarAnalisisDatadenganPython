import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
day_df = pd.read_csv('data\\day.csv')

# Cleaning Data
# Change the data type of 'dteday' to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Check for outliers
outlier_index = day_df[(day_df['season'] == 1) & (day_df['mnth'] == 12)].index
cleaned_day_df = day_df.drop(outlier_index)

# Exploratory Data Analysis (EDA)
# Calculate the average bike rental and group by season
average_rental = cleaned_day_df.groupby('season')['cnt'].mean().reset_index()

# Calculate the average rental per month for every season
average_rental_per_month = cleaned_day_df.groupby(['season', 'mnth'])['cnt'].mean().reset_index()

# Streamlit App
st.title('Bike Sharing Dataset Analysis')
st.subheader('By Undissya Putri Maharani')

# Pertanyaan 1: Which season has the most customers? And can you show the trend for each weather?
st.header('Pertanyaan 1: Which season has the most customers? And can you show the trend for each weather?')

# Visualization: Bar chart of average bike rentals in every season
plt.figure(figsize=(10, 6))
plt.bar(average_rental['season'], average_rental['cnt'], color=['green', 'purple', 'red', 'blue'])
plt.title('Average Bike Rentals in Every Season')
plt.xticks(average_rental['season'], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.xlabel('Season')
plt.ylabel('Average Bike Rentals')
st.pyplot(plt)

# Visualization: Line chart of trend of average bike rentals per month for every season
plt.figure(figsize=(12, 8))
plt.title('Trend of Average Bike Rentals per Month for Every Season')
plt.xlabel('Month')
plt.ylabel('Average Bike Rentals')
for season_code, color in zip(range(1, 5), ['green', 'purple', 'red', 'blue']):
    subset = average_rental_per_month[average_rental_per_month['season'] == season_code]
    plt.plot(subset['mnth'], subset['cnt'], color=color)
st.pyplot(plt)

# Pertanyaan 2: How does the comparison between the number of casual users and registered users differ between holidays and working days?
st.header('Pertanyaan 2: How does the comparison between the number of casual users and registered users differ between holidays and working days?')

# Calculate the total number of casual and registered users during holidays and working days
total_casual_holidays = cleaned_day_df[cleaned_day_df['holiday'] == 1]['casual'].sum()
total_registered_holidays = cleaned_day_df[cleaned_day_df['holiday'] == 1]['registered'].sum()
total_casual_workingdays = cleaned_day_df[cleaned_day_df['workingday'] == 1]['casual'].sum()
total_registered_workingdays = cleaned_day_df[cleaned_day_df['workingday'] == 1]['registered'].sum()

# Visualization: Bar chart of casual and registered users during holidays
plt.figure(figsize=(10, 6))

# Plot for holidays
plt.subplot(1, 2, 1)
plt.bar(['Casual Users', 'Registered Users'], [total_casual_holidays, total_registered_holidays], color=['blue', 'green'])
plt.title('Casual Users vs Registered Users during Holidays')

# Plot for working days
plt.subplot(1, 2, 2)
plt.bar(['Casual Users', 'Registered Users'], [total_casual_workingdays, total_registered_workingdays], color=['blue', 'green'])
plt.title('Casual Users vs Registered Users during Working Days')

st.pyplot(plt)
