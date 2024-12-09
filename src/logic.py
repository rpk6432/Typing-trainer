import json

def load_texts(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def count_errors(original, user_input):
    return sum(1 for i, char in enumerate(user_input) if i < len(original) and char != original[i])