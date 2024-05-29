import streamlit as st
import time
import openai

# OpenAI API 키를 세션 상태로 저장합니다.
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

# API 키를 입력받는 함수
def input_api_key():
    st.session_state.api_key = st.text_input("OpenAI API Key", type="password")
    if st.session_state.api_key:
        st.success("API Key saved")

# API 키를 설정합니다.
if st.session_state.api_key:
    openai.api_key = st.session_state.api_key
    assistant_id = "asst_hmnS67oNCLNK80ZJ40QLAK2C"
else:
    assistant_id = None

def load_openai_client_and_assistant(api_key, assistant_id):
    client = openai.OpenAI(api_key=api_key)
    my_assistant = client.beta.assistants.retrieve(assistant_id)
    thread = client.beta.threads.create()
    return client, my_assistant, thread

def wait_on_run(run, thread, client):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def get_assistant_response(client, my_assistant, assistant_thread, user_input):
    message = client.beta.threads.messages.create(
        thread_id=assistant_thread.id,
        assistant_id=assistant_id,
        content=user_input
    )

    run = client.beta.threads.runs.create(
        thread_id=assistant_thread.id,
        assistant_id=assistant_id,
    )

    run = wait_on_run(run, assistant_thread, client)

    messages = client.beta.threads.messages.list(
        thread_id=assistant_thread.id, order="asc", after=message.id
    )

    return messages.data[0].content[0].text.value

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

def submit():
    st.session_state.user_input = st.session_state.query
    st.session_state.query = ''

st.title("Hello")

input_api_key()

if assistant_id:
    client, my_assistant, assistant_thread = load_openai_client_and_assistant(st.session_state.api_key, assistant_id)

    st.text_input("Communicate with me:", key='query', on_change=submit)
    user_input = st.session_state.user_input

    st.write("입력하세요:", user_input)

    if user_input:
        result = get_assistant_response(client, my_assistant, assistant_thread, user_input)
        st.header('assistant:blue[cool]:')
        st.text(result)
