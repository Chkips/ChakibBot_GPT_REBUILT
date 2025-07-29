import json
import os

DATA_FILE = os.path.join("data", "questions.json")

def load_data():
    """Charge les données JSON depuis le fichier."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    """Sauvegarde les données JSON dans le fichier."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)