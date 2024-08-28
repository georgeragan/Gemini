from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="WELCOME TO MY WORLD")
st.header("HI MY CHILD ASK ME 🧛")
input=st.text_input("SHOOT HERE :",key="input")
submit=st.button("PRESS HEREEEEE...")

if submit:
    response=get_gemini_response(input)
    st.subheader("Here goes the answer...")
    st.write(response)
    