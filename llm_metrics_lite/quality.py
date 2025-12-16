def quality_index(
    coherence=0,
    repetition=0,
    groundedness=0,
    readability=0,
):
    # normalize readability (rough)
    readability_norm = max(0, min(1, (readability + 100) / 200))
    return round(
        0.3 * coherence +
        0.2 * (1 - repetition) +
        0.3 * groundedness +
        0.2 * readability_norm,
        4,
    )
