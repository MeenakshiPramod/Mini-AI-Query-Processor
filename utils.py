#1. Text Cleaning

import re

def clean_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    text = text.strip().lower()
    text = re.sub(r'[^\w\s]', '', text)

    if not text:
        raise ValueError("Empty query after cleaning")

    return text

#2. Read JSON data

import json

def read_data():
    try:
        with open('data.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Data file not found.")
        return []
    

#3. Write JSON data

def write_data(data):
    try:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        log(f"Write failed: {str(e)}", level="ERROR")


#4. Logging Function

import json
from datetime import datetime

def log(message, level="INFO"):
    log_entry = {
        "timestamp": str(datetime.now()),
        "level": level,
        "message": message
    }

    with open("logs.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")