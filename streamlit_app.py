import streamlit as st
import os

pages_list = [
    st.Page(os.path.join("app", "inicio.py"), title="Inicio", icon=":material/home:", url_path="Inicio"),
    #st.Page(os.path.join("app", "tokenizer.py"), title="Tokenizador", icon=":material/robot_2:", url_path="t"),
    #st.Page(os.path.join("app", "next_word.py"), title="Próximo Token", icon=":material/robot_2:", url_path="nt"),
    st.Page(os.path.join("app", "cittripio_v1.py"), title="Version 1", icon=":material/robot_2:", url_path="v1"),
    st.Page(os.path.join("app", "cittripio_v2.py"), title="Version 2", icon=":material/robot_2:", url_path="vdos"),
    st.Page(os.path.join("app", "cittripio_v3.py"), title="Version 3", icon=":material/robot_2:", url_path="vf"),
    st.Page(os.path.join("app", "four-o-four.py"), title="404", icon=":material/robot_2:", url_path="v2"), # Do not go ahead
]

# Add the pages to the navigation
pg = st.navigation(pages_list)
pg.run()