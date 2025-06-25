# 🩺 Medical Chatbot (Streamlit + Hugging Face)

A conversational medical chatbot built with [Streamlit](https://streamlit.io/) and open-source large language models via the [Hugging Face Inference API](https://huggingface.co/inference-api).  
Ask any medical question and get helpful, conversational answers—no OpenAI key or local GPU required!

---

## 🚀 Features

- **Conversational Chat UI**: Modern, chat-style interface with chat history.
- **Powered by Open LLMs**: Uses models like Zephyr-7B (or any Hugging Face conversational model).
- **No OpenAI/credit card needed**: Uses free-tier Hugging Face API.
- **Easy to Deploy**: One-click deploy on Streamlit Community Cloud.
- **Clear Chat & Disclaimer**: Reset chat and see a medical disclaimer.

---

## 🖥️ Demo

![Demo Screenshot](demo_screenshot.png) <!-- Add your screenshot here -->

---

## 🛠️ Setup & Usage

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a Hugging Face API token

- Sign up at [huggingface.co](https://huggingface.co/)
- Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
- Create a token with **"Read"** and **"Inference Endpoints"** permissions

### 4. Add your token to Streamlit secrets

Create a file at `.streamlit/secrets.toml`:

```
hf_token = "YOUR_HF_TOKEN"
```

Or set as an environment variable:

```bash
export HF_API_TOKEN=YOUR_HF_TOKEN
```

### 5. Run the app

```bash
streamlit run chatbot.py
```

---

## 🌐 Deploy Online (Streamlit Community Cloud)

1. Push your code to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and deploy your repo.
3. Set your Hugging Face token in the app’s **Secrets** settings.

---

## 🧠 Model

- Default: [`HuggingFaceH4/zephyr-7b-beta`](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)
- You can swap in any public conversational model by changing the `model` argument in `chatbot.py`.

---

## ⚠️ Disclaimer

This chatbot is for informational purposes only and **not a substitute for professional medical advice, diagnosis, or treatment**. Always consult a healthcare professional for serious concerns.

---

## 📄 License

MIT

---

##
