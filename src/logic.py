import json

def load_texts(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
