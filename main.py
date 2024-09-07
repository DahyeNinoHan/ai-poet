from dotenv import load_dotenv
load_dotenv()

import streamlit as st


from langchain_community.chat_models import ChatOpenAI
chat_model = ChatOpenAI()


st.title("I am a poet AI. :sunglasses:")

content=st.text_input('Suggest the topic.')

if st.button("Request a poem"):
    with st.spinner('Wait for it...'):
        result=chat_model.predict(f"Write a poem about {content} in 5 lines")
        st.write(result)
        
