import streamlit as st    
from openai import OpenAI

# Set up OpenAI API key
def ask_openai(question, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
      engine="davinci",
      prompt=question,
      max_tokens=150
    )
    return response.choices[0].text

# Streamlit UI
st.title("Chatbot with OpenAI")
user_input = st.text_input("You:", "")
api_key = st.text_input("Enter your OpenAI API key:", type="password")

if st.button("Ask") and user_input and api_key:
    bot_response = ask_openai(user_input, api_key)
    st.write("Bot:", bot_response)
