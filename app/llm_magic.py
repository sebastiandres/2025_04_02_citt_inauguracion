import streamlit as st
import requests
import json
import os
import toml
import random
import pandas as pd
import tiktoken

import torch
from transformers import GPT2TokenizerFast, GPT2LMHeadModel

from app.streamlit_magic import get_api_key

VERBOSE = True

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


def get_tokenization(text):
    """
    Tokenizes a text using the tokenizer of the model.
    """
    enc = tiktoken.get_encoding("o200k_base")
    token_ids = enc.encode(text)
    token_str = [enc.decode([_]) for _ in token_ids]
    return token_str, token_ids


def get_next_word(user_text,max_tokens=10):
    """
    Predicts the next word in a text using the model.
    """
    t = GPT2TokenizerFast.from_pretrained("gpt2")
    m = GPT2LMHeadModel.from_pretrained("gpt2")

    user_text = user_text.strip()

    encoded_text = t(user_text, return_tensors="pt")

    #1. step to get the logits of the next token
    with torch.inference_mode():
        outputs = m(**encoded_text)

    next_token_logits = outputs.logits[0, -1, :]

    # 2. step to convert the logits to probabilities
    next_token_probs = torch.softmax(next_token_logits, -1)

    # 3. step to get the top 10
    topk_next_tokens= torch.topk(next_token_probs, max_tokens)

    #putting it together
    token_list = []
    for idx, prob in zip(topk_next_tokens.indices, topk_next_tokens.values):
        prob_str = f"{100*prob:00.2f}%"
        token_list.append([t.decode(idx), idx, prob_str])
    # Convert to pandas dataframe
    token_df = pd.DataFrame(token_list, columns=["token", "token_id", "probabilidad"])
    return token_df


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