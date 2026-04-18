import streamlit as st

st.title("Image Gallery App")

files = st.file_uploader("Upload up to 3 images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if files:
    if len(files) > 3:
        st.error("Please upload a maximum of 3 images.")
    else:
        if len(files) == 3:
            st.success("3 images uploaded successfully!")
        cols = st.columns(len(files))
        for col, img in zip(cols, files):
            col.image(img, use_container_width=True)
