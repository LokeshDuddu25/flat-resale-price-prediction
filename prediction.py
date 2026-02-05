import streamlit as st
import datetime
import pickle
import numpy as np
from pathlib import Path
import search
import time

BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_model():
    with open(BASE_DIR / "model_xg.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_mappings():
    data = search.load_all_json()
    return (
        data["flat_model"],
        data["flat_type"],
        data["street"],
        data["town"],
    )

def prediction():
    st.title("🏢 Flat Resale Price Prediction")

    flat_model_data, flat_type_data, street_data, town_data = load_mappings()

    date = st.date_input("Select Resale Date", datetime.date.today())
    month, year = date.month, date.year

    town = st.selectbox("Town", search.search_town(), index=0)
    flat_type = st.selectbox("Flat Type", search.search_flat_type(), index=0)
    street = st.selectbox("Street Name", search.search_street(), index=0)
    area = st.number_input("Floor Area (sqm)")
    flat_model = st.selectbox("Flat Model", search.search_flat_model(), index=0)

    current_year = datetime.datetime.now().year
    lease_year = st.selectbox(
        "Lease Commence Year",
        ["-- Select lease commence year --"] + list(range(1960, current_year + 1)),
        index=0
    )

    remaining_lease = None if isinstance(lease_year, str) else lease_year + 99 - year

    storey_from = st.number_input("Storey From")
    storey_to = st.number_input("Storey To")

    col1, col2 = st.columns([3, 1])
    predict_btn = col1.button("Predict Price")
    logout_btn = col2.button("Logout")

    if logout_btn:
        st.session_state.logged_in = False
        st.rerun()

    if predict_btn:
        model = load_model()

        with st.spinner("Predicting price 🚀"):
            time.sleep(2)

            data = np.array([[month,
                            town_data[town],
                            flat_type_data[flat_type],
                            street_data[street],
                            area,
                            flat_model_data[flat_model],
                            lease_year,
                            remaining_lease,
                            storey_from,
                            storey_to,
                            year]])

            predicted_price = round(model.predict(data)[0])

        st.markdown(
            f"""
            <div style="
                background-color:#cce5ff;
                color:#003366;
                padding:15px;
                border-radius:10px;
                border:2px solid #99ccff;
                font-weight:bold;
                font-size:20px;">
                🏠 Flat's Estimated Price: ${predicted_price}
            </div>
            """,
            unsafe_allow_html=True
        )
