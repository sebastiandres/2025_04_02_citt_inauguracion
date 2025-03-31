import streamlit as st
from magic import hide_sidebar

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("404 Not Found")
st.write("The page you are looking for does not exist.")