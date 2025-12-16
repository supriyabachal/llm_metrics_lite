import re
from .tokens import count_words

def numeric_density(text):
    numbers = re.findall(r"\b\d+(\.\d+)?\b", text)
    words = count_words(text)
    return round(len(numbers) / max(1, words), 4)
