import streamlit as st
import openai

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
