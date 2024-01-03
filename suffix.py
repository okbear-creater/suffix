from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('보고서체 컨버터 :page_facing_up:')

before = st.text_area("'~입니다.' 체의 글을 보고서 작성시 주로 사용하는 '~이다.' 체로 변환해드립니다. 보고서체로 변환할 글을 붙여넣으세요.")

if st.button('변환'):
    with st.spinner('변환중이에요. 곧 완료되어요.'):
        after = chat_model.predict("\'"+before +"\'"+ "이 문장들의 표현을 '~이다.' 로 바꿔줘. 예를 들어 '나는 학교에 갑니다.' 가 입력되었으면 '나는 학교에 간다.' 이런식으로. 입력한 글 내용은 바꾸거나 수정하지 마.")
        st.write(after)