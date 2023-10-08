import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.cm as cm
import seaborn as sns

def process_matrix(matrix):
    for i in range(1, len(matrix)-1):
        d1 = matrix[i] - matrix[i-1]
        d2 = matrix[i+1]-matrix[i]
        if d1>5 or d1<-5 or d2>5 or d2<-5:
            matrix[i] = matrix[i-1]
    return matrix

def convert_time_matrix(time_matrix):
    result_matrix = []
    for time_row in time_matrix:
        result_row = []
        hours, minutes = map(int, time_row.split(':'))
        total_minutes = hours * 60 + minutes

        if (total_minutes >= 8 * 60 and total_minutes < 20 * 60) or (total_minutes >= 32 * 60 and total_minutes < 44 * 60):
            result_row.append(0)
        else:
            result_row.append(1)

        result_matrix.append(result_row)

    return result_matrix

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
rssi = np.convolve(rssi, filter_window, mode='same')

# rssi = process_matrix(rssi)
plt.figure(figsize=(10, 7))

plt.plot(rssi[4:])
x_values = [180]
for value in x_values:
    plt.axvline(x=value, color='green')

valuserozshab = range(72,len(rssi[4:]),144)
valuserozroz = range(0,len(rssi[4:]),144)
for value in valuserozshab:
    plt.axvline(x=value, color='black')
for value in valuserozroz:
    plt.axvline(x=value, color='red')

plt.xlabel('Sample Number')
plt.ylabel('RSSI')
plt.tight_layout()
plt.show()

