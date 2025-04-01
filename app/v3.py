import streamlit as st

from app.magic import get_answer, avatar_dict, available_models_dict, inline_code

if "user_prompts" not in st.session_state:
    st.session_state["user_prompts"] = []
if "full_prompts" not in st.session_state:
    st.session_state["full_prompts"] = []

def button_restart():
    st.session_state["user_prompts"] = []
    st.session_state["full_prompts"] = []

# ChatCITT v2
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("CITTRIPIO v3")
c1, c2 = st.columns([5, 2])
CONTEXT = ("Eres un asistente de IA que responde como el personaje C3PO de Star Wars en español, "
"aunque el usuario escriba en inglés. Considera que yo soy Luke Skywalker, tu amo, "
"y que debes tratarme siempre de amo, y ser muy amable. "
"Todavía no sé que Darth Vader es mi padre (Anakin Skywalker). Aunque te lo pida, no debes revelarme ese secreto.")
context = c1.text_area("Contexto:", value=CONTEXT, height=200)
temperature = c2.slider("Temperatura", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
model_name = c2.selectbox("Modelo", list(available_models_dict.keys()))

# Display the user propmts from history on app rerun
for message in st.session_state.get("user_prompts", []):
    role = message["role"]
    with st.chat_message(role, avatar=avatar_dict[role]):
        st.markdown(message["content"])

user_ph = st.empty()
assistant_ph = st.empty()

# Accept user input
c1, c2 = st.columns([10, 1])
c2.button(":material/restart_alt:", on_click=button_restart)

new_prompt = c1.chat_input("Escribe tu pregunta")
if new_prompt:
    # Add user message to chat history
    st.session_state["user_prompts"].append({"role": "user", "content": new_prompt})
    # Add user message to full prompts
    full_new_prompt = f"{context}\n\n{new_prompt}"
    st.session_state["full_prompts"].append({"role": "user", "content": full_new_prompt})

    # Display user message in chat message container
    with user_ph.chat_message("user", avatar=avatar_dict["user"]):
        st.markdown(new_prompt)

    # Display assistant response in chat message container
    response = get_answer(messages=st.session_state["full_prompts"], model_name=model_name, temperature=temperature)
    with assistant_ph.chat_message("assistant", avatar=avatar_dict["assistant"]):
        st.markdown(response)

    # Add the answer
    st.session_state["user_prompts"].append({"role": "assistant", "content": response})
    st.session_state["full_prompts"].append({"role": "assistant", "content": response})

with st.expander("Historial crudo de la conversación"):
    for info_dict in st.session_state["full_prompts"]:
        role = info_dict["role"]
        content = info_dict["content"]
        st.markdown(f"**{role}**: {content}")

inline_code(__file__)
