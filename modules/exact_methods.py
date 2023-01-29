from math import fabs


def print_matrix(matrix_arg, rows, cols):
    """ Prints matrix_arg """
    print("[", end="")
    for i in range(rows):
        if (i != 0):
            print(" [", end="")
        else:
            print("[", end="")
        for j in range(cols):
            if (j != cols - 1):
                print("%7.3f" % (matrix_arg[i][j]), end=", ")
            else:
                print("%7.3f" % (matrix_arg[i][j]), end="")
        if (i != rows - 1):
            print("],")
        else:
            print("]", end="")
    print("]")


def swap_rows(matrix_arg, row_index_1, row_index_2):
    """ Swap two rows of matrix_arg """
    tmp = list(matrix_arg[row_index_1])
    matrix_arg[row_index_1] = matrix_arg[row_index_2]
    matrix_arg[row_index_2] = list(tmp)
    return matrix_arg


def reverse_gauss_method(matrix_arg, rows_arg, cols_arg):
    """ Finding the vector of roots, beginning from the last equation of linear system. """
    roots_list = [0 for i in range(rows_arg)]
    i = rows_arg - 1
    while i >= 0:
        if i == (rows_arg - 1):
            roots_list[i] = matrix_arg[i][(cols_arg - 1)] / matrix_arg[i][(cols_arg - 2)]
        else:
            roots_list[i] = matrix_arg[i][(cols_arg - 1)]  # roots_list = b(i)
            j = rows_arg - 1
            while (j > i):
                roots_list[i] -= matrix_arg[i][j] * roots_list[j]
                j -= 1
            roots_list[i] = roots_list[i] / matrix_arg[i][i]

        i -= 1

    return roots_list


def direct_gauss_method(matrix_arg, rows_arg, cols_arg):
    """ Transform system of linear equations to the equivalent linear system with the upper triangle matrix """
    multipliers_gen_counter = cols_arg - 2
    col_first_number = 0
    for i in range(cols_arg - 1):
        if i == (cols_arg - 2):
            roots_list = reverse_gauss_method(matrix_arg, rows_arg, cols_arg)
            return roots_list

        # finding the biggest element of each row and return its index
        col_max = 0
        col_max_index = 0
        for j in range(col_first_number, rows_arg):
            if (fabs(matrix_arg[j][i]) > fabs(col_max)):
                col_max = matrix_arg[j][i]
                col_max_index = j

        # swaping matrix rows (if necessary)
        if (col_max_index != i):
            matrix_arg = swap_rows(matrix_arg, i, col_max_index)
            print(f"\nThe {i} and {col_max_index} rows of matrix has been swaped!")
            print_matrix(matrix_arg, rows_arg, cols_arg)

        # changing matrix
        # finding multipliers
        multipliers_vector = [0 for elem in range(multipliers_gen_counter)]
        j = i + 1
        for k in range(multipliers_gen_counter):
            multipliers_vector[k] = -(matrix_arg[j][i] / col_max)
            j += 1

        # showing multipliers
        print("\nMultipliers (m): ", end=" ")
        for multiplier in multipliers_vector:
            print("%.3f" % (multiplier), end=" ")

        # calculating new matrix coeficients
        multipliers_index = 0
        for j in range(i + 1, rows_arg):
            for k in range(col_first_number, cols_arg):
                matrix_arg[j][k] = matrix_arg[j][k] + matrix_arg[i][k] * multipliers_vector[multipliers_index]

            multipliers_index += 1

        # Showing changed matrix
        print("\nChanged matrix:")
        print_matrix(matrix_arg, rows_arg, cols_arg)
        col_first_number += 1
        multipliers_gen_counter -= 1


def gauss_method(matrix_arg, rows_arg, cols_arg):
    """Implementation of gauss method to find roots of system of linear equations """
    roots_list_local = direct_gauss_method(matrix_arg, rows_arg, cols_arg)
    return roots_list_local