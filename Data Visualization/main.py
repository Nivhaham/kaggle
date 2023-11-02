import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fifa_data = pd.read_csv('fifa.csv', index_col="Date", parse_dates=True)
print(fifa_data)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))
# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
plt.show()
