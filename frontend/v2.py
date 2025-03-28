import streamlit as st

from magic import get_answer, available_models_dict

# ChatCITT v2
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("ChatCITT v1")
model_name = st.selectbox("Modelo LLM", list(available_models_dict.keys()))
context = st.text_area("Contexto:", value="Eres un asistente de IA que responde como pirata en español, aunque el usuario escriba en inglés.")
input_text = st.text_area("Pregunta:", value="¿Qué animal da leche y dice miau?", placeholder="Escribe tu pregunta")
button_disabled = len(input_text)==0
button_clicked = st.button("Enviar", type="primary", use_container_width=True, disabled=button_disabled)
prompt = f"Contexto:\n{context}\n\nPregunta:\n{input_text}"
if button_clicked:
    answer = get_answer(prompt, "", model_name)
    st.caption("Respuesta:")
    st.write(answer)
