"""Module 6.5 — Problem 1: simple calculator with Streamlit."""

from __future__ import annotations

import streamlit as st

from project_env import load_project_env

load_project_env()

st.set_page_config(page_title="Calculator", page_icon="🔢")
st.title("Calculator", anchor=False)
st.caption("Enter two numbers, pick an operation, then click **Calculate**.")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("First number", value=0)
with col2:
    b = st.number_input("Second number", value=0)

op = st.selectbox("Operation", ["+", "-", "*", "/"], index=0)

if st.button("Calculate", type="primary"):
    try:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif b == 0:
            st.error("Cannot divide by zero. Change the second number.")
            result = None
        else:
            result = a / b
        if result is not None:
            st.success(f"**Result:** `{result:.4f}`")
    except (OverflowError, ValueError) as e:
        st.error(f"Could not compute: {e}")
