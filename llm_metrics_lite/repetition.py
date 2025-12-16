import re

def repetition_ratio(text, n=3):
    tokens = re.findall(r"\w+", text.lower())
    if len(tokens) < n:
        return 0.0
    ngrams = list(zip(*[tokens[i:] for i in range(n)]))
    return round(1 - (len(set(ngrams)) / len(ngrams)), 4)
