import streamlit as st
import requests
import json
import os
import toml
import random

VERBOSE = True

avatar_dict = {
    "user": os.path.join("app", "images", "user.png"),
    "assistant": os.path.join("app", "images", "assistant.png")
}

def hide_sidebar():
    """
    Hides the sidebar in the Streamlit app.
    """
    if st.secrets["DISABLE_SIDEBAR"]:
        st.markdown(
        """
        <style>
            [data-testid="stSidebarCollapsedControl"] {
                display: none
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
    return


def apply_colors(token_list):
    """
    Applies colors to the token string.
    """
    colors = [":red-background[{}]", ":orange-background[{}]", ":green-background[{}]", 
                ":blue-background[{}]", ":violet-background[{}]", ":gray-background[{}]"]
    color_str = ""
    for i, it in enumerate(token_list):
        color_format = colors[i%len(colors)]
        color_str += color_format.format(str(it))
    return color_str

def get_api_key(use_streamlit=True, verbose=VERBOSE):
    """
    This reads the API key from the .streamlit/secrets.toml file
    """
    if use_streamlit:
        return st.secrets["OPENROUTER_API_KEY"]
    else:
        # Read the .streamlit/secrets.toml file
        with open(".streamlit/secrets.toml", "r") as file:
            secrets = toml.load(file)
        return secrets["OPENROUTER_API_KEY"]


@st.dialog(title="Código de la aplicación", width="large")
def popup_code(filepath):
    """
    Shows the code of the app.
    """
    with open(filepath, "r") as file:
        st.code(file.read(), language="python")


def inline_code(filepath):
    """
    Shows the code of the app.
    """
    with st.expander("Código de la aplicación"):
        with open(filepath, "r") as file:
            st.code(file.read(), language="python")