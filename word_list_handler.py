# File: word_list_handler.py
def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)