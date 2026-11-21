import streamlit as st
from services.gemini import ask_gemini


st.title("AI PDF Chat Assistant")

question = st.text_input("Ask something:")

if question:
    answer = ask_gemini(question)
    st.write(answer)