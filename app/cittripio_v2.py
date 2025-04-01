import streamlit as st

from app.streamlit_magic import hide_sidebar, popup_code
from app.llm_magic import get_answer, available_models_dict

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()

st.title("CITTRIPIO v2")
model_name = st.selectbox("Modelo LLM", list(available_models_dict.keys()))
context_str = st.text_area("Contexto:", value="Eres un asistente de IA que responde como pirata en español, aunque el usuario escriba en inglés.")
question_str = st.text_area("Pregunta:", value="¿Qué animal da leche y dice miau?", placeholder="Escribe tu pregunta")

c1, c2 = st.columns([10, 1])
button_clicked = c1.button("Enviar", type="primary", use_container_width=True, disabled=len(question_str)==0)
if button_clicked:
    full_prompt = f"Contexto:\n{context_str}\n\nPregunta:\n{question_str}"
    answer = get_answer(prompt=full_prompt, model_name=model_name)
    st.caption("Respuesta:")
    st.write(answer)

if c2.button(":material/code:", use_container_width=True, type="secondary"):
    popup_code(__file__)
