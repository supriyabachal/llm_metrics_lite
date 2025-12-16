def estimated_cost(tokens, price_per_1k=0.002):
    if tokens is None:
        return 0.0
    return round((tokens / 1000) * price_per_1k, 6)
