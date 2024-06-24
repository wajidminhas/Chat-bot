from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

try:
  genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
  st.error(f"Error configuring Generative AI: {e}")
  exit(1)

model = genai.GenerativeModel("gemini-pro")

# TO MAINTAIN CHAT HISTORY
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


st.set_page_config(page_title="Hot Line", page_icon=":robot:", layout="wide")

st.header("PIAIC Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Ask your question", key="input")
submit = st.button("Submit")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.session_state['chat_history'].append(("user", user_input))
    st.subheader("Chat Response:")
    for message in response:
        st.write(message.text)
        st.session_state['chat_history'].append(("Agent", message.text))

st.subheader("Chat History")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}") 
