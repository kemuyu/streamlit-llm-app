from dotenv import load_dotenv

load_dotenv()

import streamlit as st
st.title("健康のお悩み解決アプリ")

st.write("##### 睡眠の専門家: 良質な睡眠のアドバイス")
st.write("入力フォームに睡眠に関する質問を入力し、「実行」ボタンを押すことでアドバイスを得られます。")
st.write("##### 食事の専門家: 健康のための食事のアドバイス")
st.write("入力フォームに食事に関する質問を入力し、「実行」ボタンを押すことでアドバイスを得られます。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["睡眠の専門家", "食事の専門家"]
)

st.divider()

if selected_item == "睡眠の専門家":
    input_message = st.text_input(label="睡眠に関するお悩みを入力してください。")
else:
    input_message = st.text_input(label="食事に関するお悩みを入力してください。")

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

if st.button("実行"):
    st.divider()
    if selected_item == "睡眠の専門家":
        if input_message:
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
            SystemMessage(content="あなたは睡眠の専門家です。ユーザーからの質問に対して良質な睡眠をとるためのアドバイスを回答してください。"),
            HumanMessage(content= input_message),
            ]
            result = llm(messages)
            print(result.content)
        else:
             st.write("睡眠に関するお悩みを入力してください。")
    else:
        if input_message:
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
            SystemMessage(content="あなたは食事の専門家です。ユーザーからの質問に対して健康的な食事をとるためのアドバイスを回答してください。"),
            HumanMessage(content= input_message),
            ]
            result = llm(messages)
            print(result.content)
        else:
            st.write("食事に関するお悩みを入力してください。")


    