import streamlit as st

from magic import get_answer

# ChatCITT v1
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("ChatCITT v1")
input_text = st.text_area("Pregunta:", value="¿Qué animal da leche y dice miau?", placeholder="Escribe tu pregunta")
button_disabled = len(input_text)==0
button_clicked = st.button("Enviar", type="primary", use_container_width=True, disabled=button_disabled)
if button_clicked:
    answer = get_answer(input_text, "", "deepseek-ai/DeepSeek-V3-0324")
    st.caption("Respuesta:")
    st.write(answer)
