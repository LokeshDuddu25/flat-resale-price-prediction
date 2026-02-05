import streamlit as st
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

@st.cache_data
def load_all_json():
    def load(name):
        with open(BASE_DIR / "json_files" / name, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "town": load("town.json"),
        "street": load("street_name.json"),
        "flat_type": load("flat_type.json"),
        "flat_model": load("flat_model.json"),
    }

def search_town():
    return ["-- Select a town name --"] + list(load_all_json()["town"].keys())

def search_street():
    return ["-- Select a street name --"] + list(load_all_json()["street"].keys())

def search_flat_type():
    return ["-- Select a flat type --"] + list(load_all_json()["flat_type"].keys())

def search_flat_model():
    return ["-- Select a flat model --"] + list(load_all_json()["flat_model"].keys())
