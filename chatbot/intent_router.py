def detect_intent(question: str):
    q = question.lower()

    # COUNT HOLDINGS
    if (
        "total holdings" in q
        or "number of holdings" in q
        or "how many holdings" in q
    ):
        return "COUNT_HOLDINGS"

    # FUND PERFORMANCE
    if (
        "performed better" in q
        or "best fund" in q
        or "yearly profit" in q
        or "yearly p&l" in q
    ):
        return "FUND_PERFORMANCE"

    # COUNT TRADES
    if (
        "total trades" in q
        or "number of trades" in q
        or "how many trades" in q
    ):
        return "COUNT_TRADES"

    # CROSS DATASET (SAFE)
    if "trade" in q and "performance" in q:
        return "TRADE_VS_PERFORMANCE"

    return "UNSUPPORTED"
