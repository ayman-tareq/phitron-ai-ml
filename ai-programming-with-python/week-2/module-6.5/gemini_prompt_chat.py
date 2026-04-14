"""Module 6.5 — Problem 2: send a prompt to Gemini and show the reply."""

from __future__ import annotations

import os

import streamlit as st
from google import genai

from project_env import load_project_env

load_project_env()

MODEL = "gemini-flash-latest"


def resolve_api_key() -> str | None:
    k = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    try:
        sec = getattr(st, "secrets", None)
        if sec:
            k = k or sec.get("GOOGLE_API_KEY") or sec.get("GEMINI_API_KEY")
    except Exception:
        pass
    return k


st.set_page_config(page_title="Gemini prompt", page_icon="✨")
st.title("Gemini prompt", anchor=False)
st.caption("Type a prompt and click **Generate**.")

api_key = resolve_api_key()
if not api_key:
    st.warning(
        "Set `GEMINI_API_KEY` or `GOOGLE_API_KEY` in the project root `.env`, "
        "your environment, or `.streamlit/secrets.toml`."
    )

PROMPT_KEY = "gemini_prompt_text"


def _clear_prompt() -> None:
    st.session_state[PROMPT_KEY] = ""


if PROMPT_KEY not in st.session_state:
    st.session_state[PROMPT_KEY] = ""

prompt = st.text_area(
    "Your prompt",
    placeholder="Ask anything…",
    height=160,
    key=PROMPT_KEY,
)

cols = st.columns(2)
with cols[0]:
    gen = st.button(
        "Generate",
        type="primary",
        disabled=not api_key or not (prompt or "").strip(),
    )
with cols[1]:
    st.button("Reset", type="secondary", on_click=_clear_prompt)

if gen:
    client = genai.Client(api_key=api_key)
    try:
        with st.spinner("Calling Gemini…"):
            resp = client.models.generate_content(model=MODEL, contents=prompt.strip())
        text = (resp.text or "").strip()
        if not text:
            st.warning("The model returned an empty response.")
        else:
            st.subheader("Response")
            st.write(text)
    except Exception as e:
        st.error(f"Request failed: {e}")