import streamlit as st
ROWS = 3
COLS = 4

st.set_page_config(layout="wide")


def add_coefficients_row(row_index):
    col1, col1_2, col2, col2_2, col3, col3_2, col4, col5 = st.columns([1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 5])
    with col1:
        matrix[row_index][0] = st.number_input(label="", step=1., format="%.2f", key=f"a{(row_index+1)}1")
    with col1_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x1 + </p>', unsafe_allow_html=True)

    with col2:
        matrix[row_index][1] = st.number_input(label="", step=1., format="%.2f", key=f"a{(row_index+1)}2")
    with col2_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x2 + </p>', unsafe_allow_html=True)

    with col3:
        matrix[row_index][2] = st.number_input(label="", step=1., format="%.2f", key=f"a{(row_index+1)}3")

    with col3_2:
        st.text("")
        st.text("")
        st.markdown('<p class="big-font">x3 = </p>', unsafe_allow_html=True)

    with col4:
        matrix[row_index][3] = st.number_input(label="", step=1., format="%.2f", key=f"a{(row_index+1)}4")


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

col1, col1_2, col2, col2_2, col3, col3_2, col4, col5 = st.columns([1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 5])

with col1:
    matrix[0][0] = st.number_input(label="", step=1., format="%.2f", key="a11")
with col1_2:
    st.text("")
    st.text("")
    st.markdown('<p class="big-font">x1 + </p>', unsafe_allow_html=True)

with col2:
    matrix[0][1] = st.number_input(label="", step=1., format="%.2f", key="a12")
with col2_2:
    st.text("")
    st.text("")
    st.markdown('<p class="big-font">x2 + </p>', unsafe_allow_html=True)

with col3:
    matrix[0][2] = st.number_input(label="", step=1., format="%.2f", key="a13")
with col3_2:
    st.text("")
    st.text("")
    st.markdown('<p class="big-font">x3 = </p>', unsafe_allow_html=True)

with col4:
    matrix[0][3] = st.number_input(label="", step=1., format="%.2f", key="a14")
# add_coefficients_row(0)

method = st.radio("Select method: ", methods_list)


