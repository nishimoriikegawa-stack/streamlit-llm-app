# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

def assistant_app(mode, question):
    messages = [
        SystemMessage(content = "You are a helpful assistant."),
        HumanMessage(content = f"""
                     あなたは投資の専門家です。{mode}について以下の質問に答えてください。
                     質問: {question}"""),
    ]
    result = llm(messages)
    return result.content

st.title("投資に関する疑問解答アプリ")

st.write("下記の投資対象に関する疑問について回答します")

selected_item  = st.radio(
    "動作モードを選択してください",
    ["株式", "債券", "不動産", "コモディティ", "仮想通貨", "その他"]
)

st.divider()

if selected_item == "株式":
    st.write("株式に関する質問に答えます")
    response = assistant_app("株式", st.text_input("質問を入力してください"))

elif selected_item == "債券":
    st.write("債券に関する質問に答えます")
    response = assistant_app("債券", st.text_input("質問を入力してください"))

elif selected_item == "不動産":
    st.write("不動産に関する質問に答えます")
    response = assistant_app("不動産", st.text_input("質問を入力してください")) 

elif selected_item == "コモディティ":
    st.write("コモディティに関する質問に答えます")
    response = assistant_app("コモディティ", st.text_input("質問を入力してください"))

elif selected_item == "仮想通貨":
    st.write("仮想通貨に関する質問に答えます")
    response = assistant_app("仮想通貨", st.text_input("質問を入力してください"))

else:
    st.write("その他の投資対象に関する質問に答えます")
    response = assistant_app("その他", st.text_input("質問を入力してください"))

if st.button("質問する"):
    with st.spinner("質問中..."):
        st.write(response)