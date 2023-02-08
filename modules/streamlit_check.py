def check_matrix_coefs(matrix, rows, cols):
    row_zero_counter = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero_counter += 1
            if row_zero_counter == cols:
                return False
    return True

