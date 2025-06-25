import streamlit as st
import requests
import os

HF_API_TOKEN = st.secrets.get("hf_token") or os.getenv("HF_API_TOKEN") or "YOUR_HF_TOKEN"

def hf_chat(messages, model="HuggingFaceH4/zephyr-7b-beta"):
    # Combine messages into a single prompt
    prompt = ""
    for msg in messages:
        if msg["role"] == "user":
            prompt += f"User: {msg['content']}\n"
        else:
            prompt += f"Assistant: {msg['content']}\n"
    prompt += "Assistant: "

    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list):
            return result[0].get("generated_text", str(result[0]))
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        elif isinstance(result, dict) and "error" in result:
            return "Model is loading or unavailable. Please try again."
        else:
            return str(result)
    else:
        return f"Error: {response.text}"

st.title("Medical Chatbot 🩺🤖 (Hugging Face)")
st.markdown("Ask any medical question. This chatbot is for informational purposes only.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def display_chat():
    for msg in st.session_state.chat_history:
        role = msg["role"]
        content = msg["content"]
        css_class = "user-message" if role == "user" else "bot-message"
        st.markdown(
            f'<div class="chat-message {css_class}">{content}</div>',
            unsafe_allow_html=True,
        )

display_chat()

user_input = st.chat_input("Type your medical question...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Bot is thinking..."):
        answer = hf_chat(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    st.rerun()

if st.button("Clear chat"):
    st.session_state.chat_history = []
    st.rerun()

st.markdown(
    '<div style="margin-top:30px; color: #888; font-size: 0.9em;">'
    '<b>Disclaimer:</b> This chatbot is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</div>',
    unsafe_allow_html=True,
)