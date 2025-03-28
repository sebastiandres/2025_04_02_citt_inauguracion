import streamlit as st

from magic import get_answer, avatar_dict, available_models_dict

def button_restart():
    st.session_state["messages"] = []

# ChatCITT v2
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("ChatCITT v3")
c1, c2 = st.columns([5, 2])
input_text = c1.text_area("Contexto:", value="Eres un asistente de IA que responde como pirata en español, aunque el usuario escriba en inglés.")
temperature = c2.slider("Temperatura", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
model_name = c2.selectbox("Modelo", list(available_models_dict.keys()))

# Display chat messages from history on app rerun
messages = st.session_state.get("messages", [])
for message in messages:
    role = message["role"]
    with st.chat_message(role, avatar=avatar_dict[role]):
        st.markdown(message["content"])

user_ph = st.empty()
assistant_ph = st.empty()

# Accept user input
c1, c2 = st.columns([10, 1])
c2.button(":material/restart_alt:", on_click=button_restart)

user_prompt = c1.chat_input("Escribe tu pregunta")
if user_prompt:
    # Add user message to chat history
    full_prompt = f"{input_text}\n\n{user_prompt}"
    messages.append({"role": "user", "content": full_prompt})
    st.session_state["messages"] = messages
    # Display user message in chat message container
    role = "user"
    with user_ph.chat_message(role, avatar=avatar_dict[role]):
        st.markdown(user_prompt)

    # Display assistant response in chat message container
    role = "assistant"
    response = get_answer(full_prompt, messages, model_name)
    with assistant_ph.chat_message(role, avatar=avatar_dict[role]):
        st.markdown(response)

    # Add assistant response to chat history
    messages.append({"role": role, "content": response})
    st.session_state["messages"] = messages