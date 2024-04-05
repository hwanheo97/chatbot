# -*- coding: utf-8 -*-
"""5_1_간단한_챗봇_만들기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p3LJZO48yOW1zDQhxHBOg-HxmqxTmkoK
"""


#langchain==0.0.350에서 dependency 오류가 발생하여 기존 langchanin 삭제
#!pip3 uninstall -y langchain

#langchain==0.0.350에서 dependency 오류가 발생하여 langchanin 최신 버전으로 설치
#!pip install langchain

# langchain-community 역시 재설치
#!pip install -U langchain-community

#!pip install streamlit==1.29.0

#!pip install openai==0.28.1

import streamlit as st
from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

# Everything is accessible via the st.secrets dict:
# #st.write("DB username:", st.secrets["db_username"])
# st.write("OPENAI_API_KEY:", st.secrets["auth_token"])




st.set_page_config(page_title="🦜🔗 Ben's 인공지능 ! 질문하세요~ ")
st.title('🦜🔗 인공지능! 질문하세요~ ')



import os
#os.environ["OPENAI_API_KEY"] = "auth_token"  

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["OPENAI_API_KEY"] == st.secrets["auth_token"],
)

def generate_response(input_text):  #llm이 답변 생성
    llm = OpenAI(model_name='gpt-4-0613', temperature=0)
    st.info(llm(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기')
    generate_response(text)




#from langchain_community.chat_models import ChatOpenAI

# def generate_response(input_text):
#     llm = ChatOpenAI(model_name='gpt-4-0314', temperature=0)
#     st.info(llm(input_text))

# with st.form('Question'):
#     text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
#     submitted = st.form_submit_button('보내기')
#     generate_response(text)

