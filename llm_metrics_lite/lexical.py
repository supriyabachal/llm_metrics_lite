import re

def lexical_diversity(text):
    words = re.findall(r"\w+", text.lower())
    if not words:
        return 0.0
    return round(len(set(words)) / len(words), 4)
