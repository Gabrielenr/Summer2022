"""Exercise 15.14
This program takes the data.csv file from NOAA's website of surface temperature anomalies.
by plotting and displaying the trend, we can see that there is an upward trend in the
temperature anomalies."""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv", header=4)
plt.figure(figsize=(10, 5))
sns.regplot(x='Year', y='Value', data=df)
plt.show()
