import streamlit as st
import requests
import json
import os
import toml
import random

VERBOSE = True

avatar_dict = {
    "user": os.path.join("assets", "images", "user.png"),
    "assistant": os.path.join("assets", "images", "assistant.png")
}

available_models_dict = {
    # Name : API Call
    "Google-Gemini-2.5 (free)": "google/gemini-2.5-pro-exp-03-25:free",
    "DeepSeek-V3 (free)": "deepseek/deepseek-chat-v3-0324:free", 
    "QWEN-32b (free)": "qwen/qwq-32b:free",
    "Meta-Llama (free)": "meta-llama/llama-3.3-70b-instruct:free",
    "Mistral-Nemo (free)": "mistralai/mistral-nemo:free",
    "Gemini-Flash": "google/gemini-2.0-flash-001",
    "OpenAI-GPT-4o": "openai/gpt-4o-mini",
    "Phi-3-mini": "microsoft/phi-3-mini-128k-instruct",
}

# Default model is the first one in the available_models_dict
DEFAULT_MODEL = list(available_models_dict.keys())[-1]


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


def get_answer(prompt="", messages=list(), model_name=DEFAULT_MODEL, api_key="", temperature=None, verbose=VERBOSE):
    """
    Sends a request to the OpenRouter API to get an answer to the prompt.
    API Documentation: https://openrouter.ai/docs/quickstart
    Usage has 3 options:
    1. Provide only a propmt (no message history).
    2. Provide only a message history (no prompt. Last message should be from user).
    3. Provide both a prompt and a message history. The prompt is added as a new user message to the message history.
    Inputs:
        prompt: str, the prompt to send to the API. Optional
        messages: list, the messages to send to the API. Optional.
        model_name: str, the model to use. Optional.
        api_key: str, the API key to use. Optional.
        temperature: float, the temperature to use. Optional.
        verbose: bool, whether to print the verbose output. Optional.
    Outputs:
        response_content: str, the response content from the API.
    """
    # Get the API key
    if api_key == "":
        api_key = get_api_key(verbose=verbose)
    # Define stuff
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers_dict = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    # Append the prompt to the messages
    if len(prompt)>0:
        messages = messages + [{"role": "user", "content": prompt}]
    # Pack the data
    data_dict = {
        "model": available_models_dict[model_name],
        "messages": messages,
    }
    if temperature is not None:
        data_dict["temperature"] = temperature
    if verbose:
        print("*"*100)
        print("Model:", model_name)
        print("Data sent to API:")
        for key in data_dict.keys():
            print(f"{key}: {data_dict[key]}")
    raw_response = requests.post(url=url, headers=headers_dict, data=json.dumps(data_dict))
    # Interpret the response as json
    response_dict = raw_response.json()
    # Get the specific response
    if "choices" in response_dict:
        response_content = response_dict["choices"][0]["message"]["content"]
    elif "message" in response_dict:
        response_content = response_dict["message"]
    else:
        response_content = "Error: No response from the model"
        print("Full response (unknown keys):", response_dict)
        print("Keys: ", response_dict.keys())
    if verbose:
        print("Response:", response_content)
    return response_content


if __name__ == "__main__":
    import time
    # Get the answer
    prompt = "¿Que animal da leche y dice miau?"
    posible_models = list(available_models_dict.keys())
    N_calls = 400
    for i in range(N_calls):
        print(i)
        # Get the API Key from file .streamlit/secrets.toml (without running streamlit run)
        API_KEY = get_api_key(use_streamlit=False, verbose=True)
        # Define a random model
        model_name = posible_models[i%len(posible_models)]
        # Get the answer
        answer = get_answer(prompt, api_key=API_KEY, model_name=model_name, verbose=True)
        # Print a separator
        print("*"*100)
        # Wait .5 seconds
        time.sleep(.5)