import streamlit as st
import os

pages_list = [
    st.Page(os.path.join("frontend", "v1.py"), title="v1", icon=":material/robot_2:"),
    st.Page(os.path.join("frontend", "v2.py"), title="v2", icon=":material/robot_2:"),
    st.Page(os.path.join("frontend", "v3.py"), title="v3", icon=":material/robot_2:"),
]

# Add the pages to the navigation
pg = st.navigation(pages_list)
pg.run()