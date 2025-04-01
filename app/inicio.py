import streamlit as st
from app.magic import hide_sidebar


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
    st.write("Esta aplicación es una demostración de la tecnología de ChatCITT.")
    st.write("Puedes usarla para probar la tecnología de ChatCITT.")
    st.write("Para usar la aplicación, simplemente haz clic en el botón de la barra de navegación.")
    st.write("¡Que tengas un buen día!")
