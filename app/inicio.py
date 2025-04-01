import streamlit as st
from app.streamlit_magic import hide_sidebar


if st.secrets["DISABLE_SIDEBAR"]:
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    hide_sidebar()
    st.title("Inicio")
    st.write("Bienvenido a la aplicación de ChatCITT.")
    st.write("Al finalizar el taller todas las versiones del chatbot estarán disponibles.")
else:
    st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    st.title("Inicio")
    st.write("Bienvenido a la aplicación de ChatCITT.")
    st.write("Esta aplicación contiene las actividades del taller.")
    st.write("Para usar la aplicación, simplemente haz clic en el botón de la barra de navegación.")
    st.write("¡Que tengas un buen día!")
