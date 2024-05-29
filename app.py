import streamlit as st
import openai

# 페이지 구성 설정
st.set_page_config(page_title="GPT-3.5-turbo Web App", layout="wide")

# 세션 상태 초기화
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "gpt_prompt" not in st.session_state:
    st.session_state.gpt_prompt = ""
if "gpt_response" not in st.session_state:
    st.session_state.gpt_response = None

# API 키 입력 함수
def input_api_key():
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        st.session_state.api_key = api_key
        st.success("API Key saved")

# GPT-3.5-turbo 응답 함수
@st.cache_data
def get_gpt_response(api_key, prompt):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# GPT 페이지
def gpt_page():
    st.title("GPT-3.5-turbo")
    input_api_key()

    prompt = st.text_area("Enter your question for GPT-3.5-turbo", value=st.session_state.gpt_prompt)
    if st.button("Get Response"):
        st.session_state.gpt_prompt = prompt
        st.session_state.gpt_response = get_gpt_response(st.session_state.api_key, prompt)

    if st.session_state.gpt_response:
        st.write(st.session_state.gpt_response)

# Streamlit 앱 실행
if __name__ == "__main__":
    gpt_page()
