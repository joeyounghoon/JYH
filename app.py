import openai 
import streamlit as st

title = st.text_input("Enter Your OpenAI API KEY", "chatbot")
st.write("question with gpt-3.5-turbo", title)

    
