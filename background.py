import streamlit as st
from pathlib import Path
import base64

BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_background():
    img_path = BASE_DIR / "assets" / "background.jpg"
    return base64.b64encode(img_path.read_bytes()).decode()

def background():
    encoded = load_background()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
