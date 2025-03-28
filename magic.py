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

def get_answer(prompt, messages, model_name):
    client = InferenceClient(
        provider="hyperbolic",
        api_key=st.secrets["HF_API_KEY"],
    )
    completion = client.chat.completions.create(
        model=model_name,
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