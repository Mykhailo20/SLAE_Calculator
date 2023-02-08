import streamlit as st
import numpy as np
from modules import exact_methods

ROWS = 3
COLS = 4
FILE_REQUIREMENTS = 'input_files/file_requirements.txt'

st.set_page_config(layout="wide")

st.markdown("<h4 style='text-align: center;'>Online calculator. Solution of systems of linear equations by"
            " the Gauss and LU methods</h4>", unsafe_allow_html=True)
st.markdown("""
<style>
.big-font {
    font-size: 24px !important;
}
</style>
""", unsafe_allow_html=True)
input_methods_list = ['File', 'Keyboard']
methods_list = ['Gauss', 'LU']

input_method = st.radio("Select method of entering data: ", input_methods_list)

matrix_fulfilled = False

if input_method == 'File':
    matrix_fulfilled = False

    try:
        with open(FILE_REQUIREMENTS) as file:
            file_requirements = file.readlines()

        with st.expander("File content requirements"):
            for requirement in file_requirements:
                st.text(requirement.replace("\n", ' '))
    except FileNotFoundError:
        print(f"File {FILE_REQUIREMENTS} not found!")

    uploaded_file = st.file_uploader("Drag and drop text file here")

    # If file was successfully uploaded
    if uploaded_file is not None:
        data_list = uploaded_file.getvalue().decode("utf-8").split()
        rows, cols = int(data_list[0]), int(data_list[1])
        matrix = np.zeros(rows*cols).reshape(rows, cols)
        element_counter = 2
        for i in range(rows):
            for j in range(cols):
                matrix[i, j] = float(data_list[element_counter])
                element_counter += 1
        matrix_fulfilled = True


elif input_method == 'Keyboard':
    matrix_fulfilled = False
    matrix = np.zeros(ROWS * COLS).reshape(ROWS, COLS)
    for row in range(ROWS):
        col1, col1_2, col2, col2_2, col3, col3_2, col4, col5 = st.columns([1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 5])

        with col1:
            matrix[row, 0] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}1")
        with col1_2:
            st.text("")
            st.text("")
            st.markdown('<p class="big-font">x1 + </p>', unsafe_allow_html=True)

        with col2:
            matrix[row, 1] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}2")
        with col2_2:
            st.text("")
            st.text("")
            st.markdown('<p class="big-font">x2 + </p>', unsafe_allow_html=True)

        with col3:
            matrix[row, 2] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}3")
        with col3_2:
            st.text("")
            st.text("")
            st.markdown('<p class="big-font">x3 = </p>', unsafe_allow_html=True)

        with col4:
            matrix[row, 3] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}4")

    if st.checkbox("All coefficients were entered"):
        matrix_fulfilled = True

if matrix_fulfilled:
    method = st.radio("Select method: ", methods_list)

    precision = st.slider("Select the number of digits after comma: ", 0, 8, key="precision")

    if st.button("Solve the system"):
        if method == 'Gauss':
            roots_list = exact_methods.gauss_method(matrix, ROWS, COLS)
        elif method == 'LU':
            roots_list = exact_methods.lu_method(matrix, ROWS, COLS)

        # Show result
        for index, root in enumerate(roots_list):
            st.success(f"x{index+1} = %.{precision}f" % root)




