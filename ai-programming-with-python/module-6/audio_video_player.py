import streamlit as st

st.title("Audio & Video Player App")

audio_file = st.file_uploader("Upload Audio", type=["mp3", "ogg"])
video_file = st.file_uploader("Upload Video", type=["mp4", "mkv"])

if st.button("Play"):
    if not audio_file and not video_file:
        st.error("Please upload an audio or video file first.")
    else:
        if audio_file:
            st.audio(audio_file)
        if video_file:
            st.video(video_file)
