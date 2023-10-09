import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file_path = "data/outdoor.csv"
df = pd.read_csv(file_path)

columns_to_keep = df.columns[:5]
df_pai = df[columns_to_keep]
array_pai = df_pai.to_numpy()
data = array_pai[:, 0]
time = array_pai[:, 1]
rssi = array_pai[:, 2]

window_size = 5
filter_window = np.ones(window_size) / window_size
rssi_smoothed = np.convolve(rssi, filter_window, mode='same')

plt.figure(figsize=(10, 7))
plt.plot(rssi_smoothed)
x_values = [180]
value_day_night = range(72, len(rssi_smoothed), 144)
value_day_light = range(0, len(rssi_smoothed), 144)

for value in x_values:
    plt.axvline(x=value, color='green')

for value in value_day_night:
    plt.axvline(x=value, color='black')

for value in value_day_light:
    plt.axvline(x=value, color='red')

plt.xlabel('Sample Number')
plt.ylabel('RSSI')
plt.tight_layout()
plt.show()
