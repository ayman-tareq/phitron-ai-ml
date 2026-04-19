import streamlit as st

st.title("Text Style Explorer")

text = st.text_input("Enter some text")

if text:
    st.divider()
    st.title(text)
    st.divider()
    st.header(text)
    st.divider()
    st.subheader(text)
    st.divider()
    st.text(text)
