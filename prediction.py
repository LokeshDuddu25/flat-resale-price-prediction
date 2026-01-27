import streamlit as st
import datetime
import json
import pickle
import numpy as np
from pathlib import Path
import search

BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_model():
    model_path = BASE_DIR / "model_xg.pkl"
    return pickle.load(open(model_path, "rb"))

def load_json(file_name):
    with open(BASE_DIR / "json_files" / file_name, "r") as f:
        return json.load(f)

# Load JSON mappings
flat_model_data = load_json("flat_model.json")
flat_type_data = load_json("flat_type.json")
street_data = load_json("street_name.json")
town_data = load_json("town.json")

def prediction():
    st.title("🏢 Flat Resale Price Prediction")

    # -------- INPUTS --------
    date = st.date_input("Select Resale Date", datetime.date.today())
    month, year = date.month, date.year

    town = st.selectbox(
    "Town",
    search.search_town(),
    index=0
)
    flat_type = st.selectbox(
    "Flat Type",
    search.search_flat_type(),
    index=0
)
    street = st.selectbox(
    "Street Name",
    search.search_street(),
    index=0
)
    area = st.number_input("Floor Area (sqm)")
    flat_model = st.selectbox(
    "Flat Model",
    search.search_flat_model(),
    index=0
)

    current_year = datetime.datetime.now().year
    lease_options = ["-- Select lease commence year --"] + list(range(1960, current_year + 1))

    lease_year = st.selectbox(
        "Lease Commence Year",
        lease_options,
        index=0
    )

    if lease_year == "-- Select lease commence year --":
        remaining_lease = None
    else:
        remaining_lease = lease_year + 99 - year

    storey_from = st.number_input("Storey From")
    storey_to = st.number_input("Storey To")

    # -------- BUTTONS (SAME LINE) --------
    col1, col2 = st.columns([3, 1])

    with col1:
        predict_btn = st.button("Predict Price")

    with col2:
        logout_btn = st.button("Logout")
    # -----------------------------------

    # -------- LOGOUT LOGIC --------
    if logout_btn:
        st.session_state.logged_in = False
        st.rerun()

    # -------- PREDICTION LOGIC --------
    if predict_btn:
        model = load_model()

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
