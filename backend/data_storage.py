import json
from pathlib import Path

DATA_FILE = Path("data/user_history.json")

def save_user_data(user_data):
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []
    all_data.append(user_data)
    with open(DATA_FILE, "w") as f:
        json.dump(all_data, f, indent=2)

def load_user_history():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return []
