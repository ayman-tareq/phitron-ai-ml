import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

st.title("Gemini Chatbot App")

question = st.text_input("Ask a question")

if st.button("Ask Gemini"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(question)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
