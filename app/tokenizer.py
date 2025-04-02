import streamlit as st

from app.streamlit_magic import hide_sidebar, popup_code, apply_colors
from app.llm_magic import get_tokenization

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("Tokenizador")

input_text = st.text_area("Texto", value="¿Qué animal da leche y dice miau?", placeholder="Escribe un texto a tokenizar")
c1, c2 = st.columns([10, 1])
button_clicked = c1.button("Enviar", type="primary", use_container_width=True, disabled=len(input_text)==0)
if button_clicked:
    token_str, token_ids = get_tokenization(input_text)
    st.caption("Tokenización:")
    st.write(apply_colors(token_str))
    st.write(apply_colors(token_ids))
if c2.button(":material/code:", use_container_width=True, type="secondary"):
    popup_code(__file__)

st.caption("Inspirado en [tokenizer](https://platform.openai.com/tokenizer) de OpenAI")