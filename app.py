import streamlit as st    
from openai import OpenAI

st.write("Hello!, require Any qeustions! ")
openai.api_key = st.text_input(label="your OpenAi Api key:", type="password")

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    print("OpenAI 챗봇에 오신 것을 환영합니다. 'exit'을 입력하면 종료됩니다.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("챗봇을 종료합니다. 안녕히 가세요!")
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
