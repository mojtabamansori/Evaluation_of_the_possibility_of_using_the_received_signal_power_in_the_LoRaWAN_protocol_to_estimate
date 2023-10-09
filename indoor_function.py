import numpy as np


# A function for filtering the matrix based on specific conditions
def filter_average(matrix):
    for i_filter in range(1, len(matrix) - 1):
        d1 = matrix[i_filter] - matrix[i_filter - 1]
        d2 = matrix[i_filter + 1] - matrix[i_filter]
        if d1 > 5 or d1 < -5 or d2 > 5 or d2 < -5:
            matrix[i_filter] = matrix[i_filter - 1]
    return matrix


# A function for normalizing an array
def normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    normalized_arr = (arr - min_val) / (max_val - min_val)
    return normalized_arr


# A function to convert a time matrix to a result matrix
def convert_time_matrix(time_matrix):
    result_matrix = []

    for time_row in time_matrix:
        hours, minutes = map(int, time_row.split(':'))
        total_minutes = hours * 60 + minutes
        is_peak_hours = (8 * 60 <= total_minutes < 20 * 60) or (32 * 60 <= total_minutes < 44 * 60)
        result_matrix.append([0 if is_peak_hours else 1])

    return result_matrix


# A function to calculate section averages in data
def calculate_section_averages(data, num_sections):
    max_data = np.max(data)
    min_data = np.min(data)
    d = (max_data - min_data) / num_sections
    section_averages = []

    for i in range(num_sections):
        section_min = min_data + i * d
        section_max = min_data + (i + 1) * d
        section_data = [x for x in data if section_min < x <= section_max]
        section_average = sum(section_data) / len(section_data) if len(section_data) > 0 else 0
        section_averages.append(section_average)

    return section_averages
