import streamlit as st
import requests
import os

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖AI ChatBot-CharMinds")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field
user_input = st.chat_input("Type your message...")

# ✅ Use API URL from environment
API_URL = os.getenv("API_URL")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Prepare full message history
    api_messages = [
        {"role": "user" if msg["role"] == "user" else "assistant", "content": msg["content"]}
        for msg in st.session_state.messages
    ]

    with st.spinner("Thinking..."):
        res = requests.post(f"{API_URL}/chat", json={"messages": api_messages})
        bot_reply = res.json().get("response", "")
        st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
