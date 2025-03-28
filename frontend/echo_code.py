import streamlit as st
import os

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title("Código")
with open(st.session_state["filepath"], "r") as file:
    st.code(file.read(), language="python")