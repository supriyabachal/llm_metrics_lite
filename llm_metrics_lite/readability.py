import re
from .tokens import count_words

_VOWELS = set("aeiouy")

def _estimate_syllables(word):
    word = word.lower()
    if len(word) <= 3:
        return 1
    syllables = 0
    prev = False
    for ch in word:
        is_vowel = ch in _VOWELS
        if is_vowel and not prev:
            syllables += 1
        prev = is_vowel
    return max(1, syllables)

def flesch_reading_ease(text):
    if not text:
        return 0.0
    sentences = max(1, len(re.split(r"[.!?]", text)))
    words = count_words(text)
    syllables = sum(_estimate_syllables(w) for w in re.findall(r"\w+", text))
    return round(
        206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words),
        3,
    )
