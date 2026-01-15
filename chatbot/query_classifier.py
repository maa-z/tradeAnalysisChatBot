def classify_query(question: str) -> str:
    q = question.lower()

    if "holding" in q or "performance" in q or "p&l" in q:
        return "holdings"

    if "trade" in q or "buy" in q or "sell" in q:
        return "trades"

    return "unsupported"
