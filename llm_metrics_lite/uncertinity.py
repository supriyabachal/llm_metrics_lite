import re

_HEDGE_TERMS = {
    "may","might","possibly","could","cannot",
    "unsure","unknown","likely","approximately",
    "as","assume","suggest"
}

def uncertainty_score(text):
    words = re.findall(r"\w+", text.lower())
    if not words:
        return 0.0
    return round(sum(w in _HEDGE_TERMS for w in words) / len(words), 4)
