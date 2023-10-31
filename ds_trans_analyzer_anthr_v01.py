import streamlit as st
from chat_openai import ChatOpenAI

# Create ChatOpenAI object
chat = ChatOpenAI(model="claude")

# Get input text 
text = st.text_input("Enter text")

if text:
  # Call Claude API
  response = chat(text)

  # Extract Claude's response
  claude_text = response["message"]

  # Display analysis
  st.write("Claude:", claude_text)
