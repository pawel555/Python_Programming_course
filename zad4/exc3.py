import collections

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Crime_Data_from_2010_small.csv')

# df['Time Occurred'] = df['Time Occurred'] * 0.01

hours = df['Time Occurred'].values
k = 0
for hour in hours:
    hours[k] = round(hour * 0.01)
    k += 1

cnt = collections.Counter(hours)

# num_bins = 12
num_bins = 24

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
counts, bins, patches = ax.hist(hours, num_bins, facecolor='blue', alpha=0.5, edgecolor='black', linewidth=1.2,
                                range=[min(hours), max(hours)])
ax.set_xticks(bins)
plt.xlabel('Hour')
plt.ylabel('No. of reports')

ax2.scatter(list(cnt.keys()), list(cnt.values()))
ax2.annotate(f'The maximum value: {max(list(cnt.values()))}', xytext=(3, 160), xy=(19, 171),
             arrowprops=dict(arrowstyle="->", lw=2))

fig.show()
fig2.show()
