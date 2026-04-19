"""Module 6.5 — Problem 3: improve a sentence professionally with Gemini."""

from __future__ import annotations

import os

import streamlit as st
from google import genai

from project_env import load_project_env

load_project_env()

MODEL = "gemini-flash-latest"
INSTRUCTION = "Improve this sentence professionally"


def resolve_api_key() -> str | None:
    k = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    try:
        sec = getattr(st, "secrets", None)
        if sec:
            k = k or sec.get("GOOGLE_API_KEY") or sec.get("GEMINI_API_KEY")
    except Exception:
        pass
    return k


def build_contents(user_sentence: str) -> str:
    s = user_sentence.strip()
    return f"{INSTRUCTION}:\n\n{s}"


st.set_page_config(page_title="Sentence improver", page_icon="✍️")
st.title("Professional sentence improver")
st.caption(
    "Your text is sent to Gemini with the instruction: "
    f"“{INSTRUCTION}”."
)

api_key = resolve_api_key()
if not api_key:
    st.warning(
        "Set `GEMINI_API_KEY` or `GOOGLE_API_KEY` in the project root `.env`, "
        "your environment, or `.streamlit/secrets.toml`."
    )

SENTENCE_KEY = "gemini_sentence_input"


def _clear_sentence() -> None:
    st.session_state[SENTENCE_KEY] = ""


if SENTENCE_KEY not in st.session_state:
    st.session_state[SENTENCE_KEY] = ""

sentence = st.text_input(
    "Sentence",
    placeholder='e.g. "i want job"',
    key=SENTENCE_KEY,
)

cols = st.columns(2)
with cols[0]:
    improve = st.button(
        "Improve",
        type="primary",
        disabled=not api_key or not sentence.strip(),
    )
with cols[1]:
    st.button("Reset", type="secondary", on_click=_clear_sentence)

if improve:
    client = genai.Client(api_key=api_key)
    try:
        with st.spinner("Improving…"):
            resp = client.models.generate_content(
                model=MODEL,
                contents=build_contents(sentence),
            )
        text = (resp.text or "").strip()
        if not text:
            st.warning("The model returned an empty response.")
        else:
            st.subheader("Improved version")
            st.write(text)
    except Exception as e:
        st.error(f"Request failed: {e}")
