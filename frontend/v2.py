import streamlit as st

from magic import get_answer, available_models_dict, hide_sidebar

# ChatCITT v2
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("CITTRIPIO v2")
model_name = st.selectbox("Modelo LLM", list(available_models_dict.keys()))
context_str = st.text_area("Contexto:", value="Eres un asistente de IA que responde como pirata en español, aunque el usuario escriba en inglés.")
question_str = st.text_area("Pregunta:", value="¿Qué animal da leche y dice miau?", placeholder="Escribe tu pregunta")
button_disabled = len(question_str)==0
button_clicked = st.button("Enviar", type="primary", use_container_width=True, disabled=button_disabled)
full_prompt = f"Contexto:\n{context_str}\n\nPregunta:\n{question_str}"
if button_clicked:
    answer = get_answer(prompt=full_prompt, model_name=model_name)
    st.caption("Respuesta:")
    st.write(answer)
