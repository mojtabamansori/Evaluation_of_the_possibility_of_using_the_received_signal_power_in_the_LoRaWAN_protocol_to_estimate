import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from indoor_function import calculate_section_averages


# Read data from a CSV file

file_path = "data/RSSI.csv"
df = pd.read_csv(file_path)

# Select the columns needed
columns_to_keep = df.columns[:5]
df_pai = df[columns_to_keep]
array_pai = df_pai.to_numpy()

z = array_pai[:, 0]
k = z
x = array_pai[:, 1]
y = array_pai[:, 4]
x = np.sort(x)
y = np.sort(y)

# Calculate section averages
num_sections = 4
sections_x = calculate_section_averages(x, num_sections)

# Calculate sections for other data
sections_y = calculate_section_averages(y, num_sections)

# Define measurements and data
barWidth = 0.2
percentage = ["0-25", "25-50", "50-75", "75-100"]
rssi = sections_x
iso = sections_y

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(12, 8))
ax2 = ax1.twinx()
bar_width = 0.35
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
