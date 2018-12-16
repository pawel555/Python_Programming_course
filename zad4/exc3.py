import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Crime_Data_from_2010_small.csv')

hours = df['Time Occurred'].values
#print(hours)

plt.hist(hours)
plt.show()
