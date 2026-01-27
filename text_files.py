import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def show_text(title, file_name):
    st.title(title)

    text = (BASE_DIR / "Text files" / file_name).read_text(encoding="utf-8")

    # Convert new lines to <br> WITHOUT extra spacing
    text = text.strip().replace("\n", "<br>")

    st.markdown(
        f"""
        <div style="
            font-weight: bold;
            font-size: 18px;
            line-height: 1.15;   /* 👈 FIXED GAP */
            margin: 0;
            padding: 0;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

def homepage():
    show_text("Buy or Sell Your Flat Today", "Homepage.txt")

def month_year():
    show_text("📅 Month & Year", "About Month & Year.txt")

def flat_type():
    show_text("🏠 Flat Type", "About Flat Type.txt")

def flat_model():
    show_text("🏢 Flat Model", "About Flat Model.txt")

def storey_range():
    show_text("🏙️ Storey Range", "About Storey Range.txt")

def table_model():
    df = pd.read_csv(BASE_DIR / "Text files" / "table_flat_model.txt")
    df.index = range(1, len(df) + 1)
    st.dataframe(df, use_container_width=True)

def table_type():
    df = pd.read_csv(
        BASE_DIR / "Text files" / "table_flat_type.txt",
        delimiter="|"
    )
    df.index = range(1, len(df) + 1)
    st.dataframe(df, use_container_width=True)
