import streamlit as st
st.set_page_config(layout="wide")

import background
import login
import register
import text_files
import prediction

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

background.background()

if st.session_state.logged_in:
    text_files.month_year()
    text_files.flat_type()
    text_files.table_type()
    text_files.flat_model()
    text_files.table_model()
    text_files.storey_range()
    prediction.prediction()
else:
    text_files.homepage()
    tab1, tab2 = st.tabs(["Login", "Register"])
    with tab1:
        login.login_ui()
    with tab2:
        register.register_ui()
