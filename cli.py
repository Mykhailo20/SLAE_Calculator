from modules import exact_methods

# main
choice_text = """Please, enter the method of entering data:
1 - keyboard input;
2 - read from a file.
Your choice: """
choice = input(choice_text)

if("1" in choice):
    dimension_list = input("Enter the dimension of matrix: ").split(" ")
    rows, cols = [int(dimension_list[0]), int(dimension_list[1])]

    matrix = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        row_coefficients = input(f"Enter the coefficients of {i+1} equation: ").split(" ")
        for j in range(cols):
            matrix[i][j] = float(row_coefficients[j])

else:
    filepath = input("Enter the file name: ")
    try:
        with open(filepath, "r") as file:
            input_list = file.readlines()
    except FileNotFoundError:
        file_error = """
The file with this name/path does not exist.
Please check if the file exists and restart the program.
"""
        print(file_error)
        exit()
    dimension_list = input_list[0].split(" ")
    rows, cols = [int(dimension_list[0]), int(dimension_list[1])]

    matrix = [[0 for j in range(cols)] for i in range(rows)]

    # Reading coefficients
    for i in range(1, (rows+1)):
        row_coefficients = input_list[i].split(" ")
        for j in range(cols):
            matrix[(i-1)][j] = float(row_coefficients[j])

"""matrix = [[1.26, -2.34, 1.17, 3.14],
          [0.75, 1.24, -0.48, -1.17],
          [3.44, -1.85, 1.16, 1.83]]
"""

print("Initial matrix: ")
exact_methods.print_matrix(matrix, 3, 4)

print("\nGauss method:")
roots_list = exact_methods.gauss_method(matrix, 3, 4)

print("\nRoots are: ", end=" ")
for root in roots_list:
    print("%.5f"%(root), end=" ")

print('\n')

