import streamlit as st
from app.magic import hide_sidebar
from random import randint
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("404 Not Found")
st.write("Estos no son los androides que estáis buscando.")
n = randint(1,3)
images_list = ["404v1.jpg", "404v2.jpg", "404v3.jpeg"]
image404 = os.path.join("app", "images", images_list[n-1])
st.image(image404, width=700)
