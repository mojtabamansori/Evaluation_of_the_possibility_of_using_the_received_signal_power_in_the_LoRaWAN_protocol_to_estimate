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


def normalize(arr):
    # یافتن مقدار حداقل و حداکثر آرایه
    min_val = np.min(arr)
    max_val = np.max(arr)

    # نرمالایز کردن آرایه به مقیاس 0 تا 1
    normalized_arr = (arr - min_val) / (max_val - min_val)

    return normalized_arr



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

file_path = "data/RSSI.csv"
df = pd.read_csv(file_path)

columns_to_keep = df.columns[:5]
df_pai = df[columns_to_keep]
array_pai = df_pai.to_numpy()

z = array_pai[:, 0]
k=z
x = array_pai[:, 1]
y = array_pai[:, 4]
x = np.sort(x)
y = np.sort(y)

a1 = []
a2 = []
a3 = []
a4 = []
max = np.max(x)
min = np.min(x)
d = (max - min)/4
for i in range(len(x)):
    if min < x[i] < (min+d):
        a1.append(x[i])
    if (min+d) < x[i] < (min+d+d):
        a2.append(x[i])
    if (min+d+d) < x[i] < (min+d+d+d):
        a3.append(x[i])
    if (max - d) < x[i] < max:
        a4.append(x[i])
a1 = sum(a1)/len(a1)
a2 = sum(a2)/len(a2)
a3 = sum(a3)/len(a3)
a4 = sum(a4)/len(a4)


x = y
ay1 = []
ay2 = []
ay3 = []
ay4 = []
max = np.max(x)
min = np.min(x)
d = (max - min)/4
for i in range(len(x)):
    if min < x[i] < (min+d):
        ay1.append(x[i])
    if (min+d) < x[i] < (min+d+d):
        ay2.append(x[i])
    if (min+d+d) < x[i] < (min+d+d+d):
        ay3.append(x[i])
    if (max - d) < x[i] < max:
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

# Create twin Axes sharing the xaxis
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

# br1 = np.arange(len(rssi))
# print(br1)
# br2 = [x + barWidth for x in br1]
# ax1 = fig.add_subplot(111)
#
# ax1.bar(br1, iso, color='r', width=barWidth,
#         edgecolor='grey', label='Soil Moisture Sensor Value')
# ax2 = fig.add_subplot(111, frame_on=False)
# ax2.bar(br2, rssi, color='blue', width=barWidth,
#         edgecolor='grey', label='RSSI')
#
# plt.xlabel('Percentage', fontweight='bold', fontsize=15)
# plt.ylabel('Sample Count', fontweight='bold', fontsize=15)
# plt.xticks([r + barWidth for r in range(len(rssi))],
#            ['0%-25%', '25%-50% ', '50%-75%', '75%-100%'])
# ax1.set_xlabel('Percentage', c='red')
# ax1.set_ylabel('RSSI', c='red')
# ax2.xaxis.tick_top()
# ax2.yaxis.tick_right()
# ax2.xaxis.set_label_position('top')
# ax2.yaxis.set_label_position('right')
# ax2.set_xlabel('Percentage', c='blue')
# ax2.set_ylabel('Soil Moisture Sensor Value', c='blue')
#
# plt.show()
#
# window_size = 5
# filter_window = np.ones(window_size) / window_size
# x = np.convolve(x, filter_window, mode='same')
# ktghir = array_pai[:, 2]
# darsdy = normalize(y)
#
# darsdy = darsdy * 100
#
# fig = plt.figure(figsize=(10, 7))
#
# x1 = [25,50,75,100]
# y1 = [a1, a2, a3, a4]
# ax1 = fig.add_subplot(111)
# ax1.plot(x1,y1, 'o--', c='red')
# plt.ylim([550,1100])
#
# x1 = [25,50,75,100]
# y1 = [ay1, ay2, ay3, ay4]
# ax2 = fig.add_subplot(111, frame_on=False)
# ax2.plot(x1,y1, 's--', c='blue')
# plt.ylim([-107,-90])
#
# # plt.xlabel('RSSI')
# # plt.ylabel('Soil Moisture Sensor Value')
# ax1.set_xlabel('Percentage', c='red')
# ax1.set_ylabel('Soil Moisture Sensor Value', c='red')
# ax2.xaxis.tick_top()
# ax2.yaxis.tick_right()
#
# ax2.xaxis.set_label_position('top')
# ax2.yaxis.set_label_position('right')
# ax2.set_xlabel('Percentage', c='blue')
# ax2.set_ylabel('RSSI', c='blue')
# # ###    plot indoor rssi   ###
# # plt.figure(figsize=(10, 7))
# # plt.plot((x[5:225]))
# # x_values = [48, 99]
# # valuserozshab = range(22,231,48)
# # valuserozroz = range(46,231,48)
# # for value in x_values:
# #     plt.axvline(x=value, color='green')
# # for value in valuserozshab:
# #     plt.axvline(x=value, color='black')
# # for value in valuserozroz:
# #     plt.axvline(x=value, color='red')
# # plt.xlabel('Sample Number')
# # plt.xticks(range(0,231,40))
# # plt.ylabel('RSSI ')
# # # plt.title(f'Plot rssi indoor')
# # plt.tight_layout()
# # plt.show()
# # z = convert_time_matrix(z)
# # z = np.array(z)
# #
# # index_roz = np.argwhere(z==0)[:,0]
# # index_shab = np.argwhere(z==1)[:,0]
# # index_dry = np.argwhere(y>=800)[:,0]
# # index_wet = np.argwhere(y<800)[:,0]
# #
# # #plot roz wet
# #
# # index_roz_wet =[]
# # for i in index_roz:
# #     for i2 in index_wet:
# #         if i ==i2:
# #             index_roz_wet.append(i)
# # index_roz_wet = np.array(index_roz_wet)
# #
# # index_roz_dry =[]
# # for i in index_roz:
# #     for i2 in index_dry:
# #         if i ==i2:
# #             index_roz_dry.append(i)
# # index_roz_dry = np.array(index_roz_dry)
# #
# # index_shab_wet =[]
# # for i in index_shab:
# #     for i2 in index_wet:
# #         if i ==i2:
# #             index_shab_wet.append(i)
# # index_shab_wet = np.array(index_shab_wet)
# #
# # index_shab_dry =[]
# # for i in index_shab:
# #     for i2 in index_dry:
# #         if i ==i2:
# #             index_shab_dry.append(i)
# # index_shab_dry = np.array(index_shab_dry)
# #
# #
# # plt.figure(figsize=(10, 7))
# # plt.scatter(x[index_roz_wet], y[index_roz_wet], c='black',s= 10)
# # plt.ylim([600,1100])
# # plt.xlim([-110,-90])
# # plt.xticks([-110,-105,-100,-95,-90])
# # plt.xlabel('RSSI')
# # plt.ylabel('Soil Moisture Sensor Value')
# # # plt.title(f'Day and Wet')
# # plt.tight_layout()
# # plt.show()
# #
# # plt.figure(figsize=(10, 7))
# # plt.scatter(x[index_roz_dry], y[index_roz_dry], c='black',s= 10)
# # plt.xlabel('RSSI')
# # plt.ylabel('Soil Moisture Sensor Value')
# # plt.ylim([600,1100])
# # plt.xlim([-110,-90])
# # plt.xticks([-110,-105,-100,-95,-90])
# # # plt.title(f'Day and Dry')
# # plt.tight_layout()
# # plt.show()
# #
# #
# # plt.figure(figsize=(10, 7))
# # plt.scatter(x[index_shab_wet], y[index_shab_wet], c='black',s= 10)
# # plt.ylim([600,1100])
# # plt.xlim([-110,-90])
# # plt.xlabel('RSSI')
# # plt.ylabel('Soil Moisture Sensor Value')
# # plt.xticks([-110,-105,-100,-95,-90])
# # # plt.title(f'Night and Wet')
# # plt.tight_layout()
# # plt.show()
# #
# # plt.figure(figsize=(10, 7))
# # plt.scatter(x[index_shab_dry], y[index_shab_dry], c='black',s= 10)
# # plt.ylim([600,1100])
# # plt.xlim([-110,-90])
# # plt.xlabel('RSSI')
# # plt.ylabel('Soil Moisture Sensor Value')
# # plt.xticks([-110,-105,-100,-95,-90])
# # # plt.title(f'Night and Dry')
# # plt.tight_layout()
# #
# #
# # plt.show()
