import streamlit as st
import os

file_filepath = os.path.join("frontend", "v3.py")
code_filepath = os.path.join("frontend", "echo_code.py")
st.session_state["filepath"] = file_filepath
pages_list = [
    st.Page(file_filepath, title="ChatCITT", icon=":material/robot_2:"),
    st.Page(code_filepath, title="código", icon=":material/checklist:"),
]

# Add the pages to the navigation
pg = st.navigation(pages_list)
pg.run()