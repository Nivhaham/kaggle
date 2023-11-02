import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
fifa_data = pd.read_csv('fifa.csv', index_col="Date", parse_dates=True)
print(fifa_data)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))
# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
plt.show()
'''
'''
spotify_data = pd.read_csv('spotify.csv', index_col="Date", parse_dates=True)
print(spotify_data)

plt.figure(figsize=(14,6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data)
plt.show()

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
plt.show()
'''

flight_data = pd.read_csv('flight_delays.csv', index_col="Month",parse_dates=True)
print(flight_data)

# Set the width and height of the figure
plt.figure(figsize=(10,6))
# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")
plt.show()