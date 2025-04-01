import streamlit as st

from app.streamlit_magic import hide_sidebar, popup_code
from app.llm_magic import get_answer

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("CITTRIPIO v1")

input_text = st.text_area("Pregunta:", value="¿Qué animal da leche y dice miau?", placeholder="Escribe tu pregunta")
c1, c2 = st.columns([10, 1])
button_clicked = c1.button("Enviar", type="primary", use_container_width=True, disabled=len(input_text)==0)
if button_clicked:
    answer = get_answer(prompt=input_text)
    st.caption("Respuesta:")
    st.write(answer)
if c2.button(":material/code:", use_container_width=True, type="secondary"):
    popup_code(__file__)
