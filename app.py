import streamlit as st    
from openai import OpenAI

import streamlit as st
import openai

# 페이지 구성 설정
st.set_page_config(page_title="OpenAI API Web App", layout="wide")

# 세션 상태 초기화
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "gpt_prompt" not in st.session_state:
    st.session_state.gpt_prompt = ""
if "dalle_prompt" not in st.session_state:
    st.session_state.dalle_prompt = ""
if "gpt_response" not in st.session_state:
    st.session_state.gpt_response = None
if "dalle_response" not in st.session_state:
    st.session_state.dalle_response = None

# API 키 입력 함수
def input_api_key():
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        st.session_state.api_key = api_key
        st.success("API Key saved")

# GPT-3.5-turbo 응답 함수
@st.cache_data
def get_gpt_response(prompt):
    openai.api_key = st.session_state.api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# Dall-E 이미지 생성 함수
@st.cache_data
def get_dalle_image(prompt):
    openai.api_key = st.session_state.api_key
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response["data"][0]["url"]

# GPT 페이지
def gpt_page():
    st.title("GPT-3.5-turbo")
    input_api_key()

    prompt = st.text_area("Enter your prompt for GPT-3.5-turbo", value=st.session_state.gpt_prompt)
    if st.button("Get Response"):
        st.session_state.gpt_prompt = prompt
        st.session_state.gpt_response = get_gpt_response(prompt)

    if st.session_state.gpt_response:
        st.write(st.session_state.gpt_response)

# Dall-E 페이지
def dalle_page():
    st.title("Dall-E Image Generator")
    input_api_key()

    prompt = st.text_area("Enter your prompt for Dall-E", value=st.session_state.dalle_prompt)
    if st.button("Generate Image"):
        st.session_state.dalle_prompt = prompt
        st.session_state.dalle_response = get_dalle_image(prompt)

    if st.session_state.dalle_response:
        st.image(st.session_state.dalle_response)

# 페이지 라우팅
page = st.sidebar.selectbox("Choose a page", ["GPT-3.5-turbo", "Dall-E"])

if page == "GPT-3.5-turbo":
    gpt_page()
else:
    dalle_page()

# Streamlit 앱 실행
if __name__ == "__main__":
    st.run()
