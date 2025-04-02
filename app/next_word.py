import streamlit as st

from app.streamlit_magic import hide_sidebar, popup_code, apply_colors
from app.llm_magic import get_next_word

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_sidebar()
st.title("Predicción de próximo token")

input_text = st.text_area("Texto", value="One, two, three, four, five and", placeholder="")
c1, c2 = st.columns([10, 1])
button_clicked = c1.button("Enviar", type="primary", use_container_width=True, disabled=len(input_text)==0)
if button_clicked:
    token_df = get_next_word(input_text)
    st.caption("Próximo token:")
    st.dataframe(token_df, hide_index=True)
if c2.button(":material/code:", use_container_width=True, type="secondary"):
    popup_code(__file__)

st.caption("Inspirado en [NextTokenPrediction](https://huggingface.co/spaces/alonsosilva/NextTokenPrediction) de Alonso Silva")