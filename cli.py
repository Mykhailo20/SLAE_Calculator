from modules import exact_methods

# main
choice_text = """Please, enter the method of entering data:
1 - keyboard input;
2 - read from a file.
Your choice: """
method_choice = """Please, enter the method of solving the SLAE:
1 - Gauss method;
2 - LU method.
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

print("Initial matrix: ")
exact_methods.print_matrix(matrix, 3, 4)

choice = input(method_choice)

if "1" in choice:
    print("\nGauss method:")
    roots_list = exact_methods.gauss_method(matrix, 3, 4)

elif "2" in choice:
    print("LU - method:")
    roots_list = exact_methods.lu_method(matrix, 3, 4)

else:
    print("""You entered the wrong number.
          Please restart the program and try again!
          """)
    exit()

print("\nRoots are: ", end=" ")
for root in roots_list:
    print("%.5f"%(root), end=" ")

print('\n')


