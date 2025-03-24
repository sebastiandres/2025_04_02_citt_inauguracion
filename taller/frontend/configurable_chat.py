import streamlit as st
import requests
import json
import os

from huggingface_hub import InferenceClient


avatar_dict = {
    "user": os.path.join("assets", "images", "user.png"),
    "assistant": os.path.join("assets", "images", "citt.png")
}

available_models_dict = {
    # Name : API Call
    "DeepSeek-V3": "deepseek-ai/DeepSeek-V3-0324",
    "Llama-3.1": "meta-llama/Llama-3.1-8B-Instruct",
    "Perplexity-Mini": "perplexity-ai/mini-perplexity-2-mini-2024-02-15",
    "Qwen":"Qwen/QwQ-32B", 
}

def button_restart():
    st.session_state["messages"] = []

def get_answer(prompt, messages, model_name):
    client = InferenceClient(
        provider="hyperbolic",
        api_key=st.secrets["HF_API_KEY"],
    )
    completion = client.chat.completions.create(
        model=available_models_dict[model_name],
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=500,
    )
    # Get the full response
    model_response = completion.choices[0].message
    # Get the specific response
    response_content = model_response.content
    return response_content


def get_answer_old(prompt, messages):
    return prompt[::-1]


def page_content():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.title("ChatCITT v2")
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


# Conditionally render the page content
page_content()