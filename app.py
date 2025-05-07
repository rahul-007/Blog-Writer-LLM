import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

## load_dotenv()
## groq_api_key = os.getenv("GROQ_API_KEY")

st.title("Blog Writer")
st.write("This blog writer is capable of writing blogs on any generic topic")

groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type='password')
if groq_api_key:
    llm = ChatGroq(model="Llama3-70b-8192",groq_api_key=groq_api_key)

## response = llm.invoke("hello, how are you?")
## print(response.content)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt_template = """You are a content writer and have specializtion in 
                    wrting blogs in easy language so that anyone can undertand it.
                    Write a blog of 200-300 words on the following topic: {input} 
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_template), 
    ("user", "{input}")
])

parser = StrOutputParser()

user_input = st.text_input("Enter any topic of your interest")
if user_input and groq_api_key:
    with st.spinner("I am thinking..."):
        chain = prompt | llm | parser
        result = chain.invoke({"input": user_input})
        print(result)
        st.success(result)
else:
    url = 'https://console.groq.com/docs/quickstart'
    st.warning("If you don't have Groq API key, get it easily by following the page:" + url)
