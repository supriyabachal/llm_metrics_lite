import re
_WORD_RE=re.compile(r"\w+")
def count_words(t): return len(_WORD_RE.findall(t or ""))
def count_characters(t,include_spaces=True):
    if not t: return 0
    return len(t) if include_spaces else len("".join(ch for ch in t if not ch.isspace()))
def approximate_token_count(t): return int(count_words(t)*1.3)
