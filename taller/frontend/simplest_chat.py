import streamlit as st
import requests
import json
import os

def get_answer(prompt):
    return prompt[::-1]

def page_content():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.title("ChatCITT v1")
    c1, c2 = st.columns([5, 1])
    input_text = c1.text_input("Pregunta:", placeholder="Escribe tu pregunta")
    c2.write(""); c2.write("")
    button_clicked = c2.button("Enviar", type="primary", use_container_width=True)

    if len(input_text) > 0 and button_clicked:
        answer = get_answer(input_text)
        st.caption("Respuesta:")
        st.write(answer)

# Conditionally render the page content
page_content()