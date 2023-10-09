import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.cm as cm
import seaborn as sns


def filter_average(matrix):
    for i_filter in range(1, len(matrix)-1):
        d1 = matrix[i_filter] - matrix[i_filter-1]
        d2 = matrix[i_filter+1]-matrix[i_filter]
        if d1 > 5 or d1 < -5 or d2 > 5 or d2 < -5:
            matrix[i_filter] = matrix[i_filter-1]
    return matrix


def normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    normalized_arr = (arr - min_val) / (max_val - min_val)
    return normalized_arr


def convert_time_matrix(time_matrix):
    result_matrix = []

    for time_row in time_matrix:
        hours, minutes = map(int, time_row.split(':'))
        total_minutes = hours * 60 + minutes
        is_peak_hours = (8 * 60 <= total_minutes < 20 * 60) or (32 * 60 <= total_minutes < 44 * 60)
        result_matrix.append([0 if is_peak_hours else 1])

    return result_matrix


file_path = "data/RSSI.csv"
df = pd.read_csv(file_path)

columns_to_keep = df.columns[:5]
df_pai = df[columns_to_keep]
array_pai = df_pai.to_numpy()

z = array_pai[:, 0]
k = z
x = array_pai[:, 1]
y = array_pai[:, 4]
x = np.sort(x)
y = np.sort(y)

# section data
a1 = []
a2 = []
a3 = []
a4 = []
max_data = np.max(x)
min_data = np.min(x)
d = (max_data - min_data)/4
for i in range(len(x)):
    if min_data < x[i] < (min_data+d):
        a1.append(x[i])
    if (min_data+d) < x[i] < (min_data+d+d):
        a2.append(x[i])
    if (min_data+d+d) < x[i] < (min_data+d+d+d):
        a3.append(x[i])
    if (max_data - d) < x[i] < max_data:
        a4.append(x[i])
a1 = sum(a1)/len(a1)
a2 = sum(a2)/len(a2)
a3 = sum(a3)/len(a3)
a4 = sum(a4)/len(a4)

# section label
x = y
ay1 = []
ay2 = []
ay3 = []
ay4 = []
max_data = np.max(x)
min_label = np.min(x)
d = (max_data - min_label)/4
for i in range(len(x)):
    if min_label < x[i] < (min_label+d):
        ay1.append(x[i])
    if (min_label+d) < x[i] < (min_label+d+d):
        ay2.append(x[i])
    if (min_label+d+d) < x[i] < (min_label+d+d+d):
        ay3.append(x[i])
    if (max_data - d) < x[i] < max_data:
        ay4.append(x[i])
ay1 = sum(ay1)/len(ay1)
ay2 = sum(ay2)/len(ay2)
ay3 = sum(ay3)/len(ay3)
ay4 = sum(ay4)/len(ay4)
barWidth = 0.2

percentage = ["0-25", "25-50", "50-75", "75-100"]
rssi = [a1, a2, a3, a4]
iso = [ay1, ay2, ay3, ay4]

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create twin Axes sharing the x_axis
ax2 = ax1.twinx()

# Bar width
bar_width = 0.35

# Bar positions
positions = np.arange(len(rssi))

# Plot bars for 'a' and 'b'
ax1.bar(positions, rssi, bar_width, label='RSSI', color='b', align='center')
ax2.bar(positions + bar_width, iso, bar_width, label='Soil Moisture Sensor Value', color='r', align='center')

# Set x-axis labels and ticks
plt.xticks(positions + bar_width / 2, percentage)

ax1.invert_yaxis()

# Set labels and title
ax1.set_xlabel('Percentage')
ax1.set_ylabel('RSSI', color='b')
ax2.set_ylabel('Soil Moisture Sensor Value', color='r')

# Show legend
ax1.legend(loc='upper left', fontsize='medium')
ax2.legend(loc='upper right', fontsize='medium')

# Show the plot
plt.show()

