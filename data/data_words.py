import random
import os
from src.config import WORDS_FILENAME

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, WORDS_FILENAME)

with open(file_path, encoding='utf-8') as file:
    words = [word for word in file.read().split() if len(word) > 3 and '-' not in word]

def get_random_word() -> str:
    return random.choice(words)