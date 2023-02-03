import streamlit as st
from modules import exact_methods


ROWS = 3
COLS = 4

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
methods_list = ['Gauss', 'LU']
matrix = [[0 for j in range(COLS)] for i in range(ROWS)]
for row in range(ROWS):
    col1, col1_2, col2, col2_2, col3, col3_2, col4, col5 = st.columns([1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 5])

    with col1:
        matrix[row][0] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}1")
    with col1_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x1 + </p>', unsafe_allow_html=True)

    with col2:
        matrix[row][1] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}2")
    with col2_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x2 + </p>', unsafe_allow_html=True)

    with col3:
        matrix[row][2] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}3")
    with col3_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x3 = </p>', unsafe_allow_html=True)

    with col4:
        matrix[row][3] = st.number_input(label="", step=1., format="%.2f", key=f"a{row+1}4")


method = st.radio("Select method: ", methods_list)

precision = st.slider("Select the number of digits after comma: ", 0, 8, key="precision")

if st.button("Solve the system"):
    if method == 'Gauss':
        roots_list = exact_methods.gauss_method(matrix, ROWS, COLS)
    elif method == 'LU':
        roots_list = exact_methods.lu_method(matrix, ROWS, COLS)

    # Show result
    result_str = "Roots are: "
    for index, root in enumerate(roots_list):
        result_str += f"x{index+1} = %.{precision}f" % root
        result_str += " "

    st.success(result_str)



