from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st

st.title("My Chat Bot Using Deepseek-R1 Model")

template = '''question: {question}
Answer = Generate the answer step by step '''

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model = "deepseek-r1")

chain = prompt | model

question = st.text_input("Enter your question here: ")

if question:
    try:
        formatted_prompt = prompt.format(question=question)

        response = chain.invoke({"question": question})

        st.write(response)
    
    except Exception as e:
        st.write(f"Error: {e}")