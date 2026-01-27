import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_json(name):
    with open(BASE_DIR / "json_files" / name, "r", encoding="utf-8") as f:
        return json.load(f)

def search_street():
    return ["-- Select a street name --"] + list(load_json("street_name.json").keys())

def search_flat_type():
    return ["-- Select a flat type --"] + list(load_json("flat_type.json").keys())

def search_flat_model():
    return ["-- Select a flat model --"] + list(load_json("flat_model.json").keys())

def search_town():
    return ["-- Select a town name --"] + list(load_json("town.json").keys())
