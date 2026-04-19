import streamlit as st

st.title("Personal Info Card App")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
profession = st.selectbox("Profession", ["Student", "Employee", "Businessman", "Freelancer"])

if st.button("Show Info Card"):
    if not name:
        st.warning("Please fill in your name.")
    else:
        st.success(f"**Name:** {name}  \n**Age:** {int(age)}  \n**Profession:** {profession}")
