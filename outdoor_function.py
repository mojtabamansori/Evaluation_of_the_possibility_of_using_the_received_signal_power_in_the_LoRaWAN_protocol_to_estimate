def process_matrix(matrix):
    for i in range(1, len(matrix) - 1):
        d1 = matrix[i] - matrix[i - 1]
        d2 = matrix[i + 1] - matrix[i]
        if abs(d1) > 5 or abs(d2) > 5:
            matrix[i] = matrix[i - 1]
    return matrix


def convert_time_matrix(time_matrix):
    result_matrix = []
    for time_row in time_matrix:
        hours, minutes = map(int, time_row.split(':'))
        total_minutes = hours * 60 + minutes

        if (8 * 60 <= total_minutes < 20 * 60) or (32 * 60 <= total_minutes < 44 * 60):
            result_matrix.append([0])
        else:
            result_matrix.append([1])

    return result_matrix
