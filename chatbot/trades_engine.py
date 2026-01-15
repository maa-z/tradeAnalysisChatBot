def total_trades(df, fund):
    data = df[df["portfolioname"].str.lower() == fund.lower()]
    return len(data)


def most_traded_security(df, fund):
    data = df[df["portfolioname"].str.lower() == fund.lower()]
    if data.empty:
        return None

    grouped = data.groupby("ticker")["quantity"].sum()
    return grouped.idxmax(), grouped.max()


def count_trades(df, fund):
    return len(df[df["portfolioname"] == fund])


def trade_volume_by_security(df, fund):
    data = df[df["portfolioname"] == fund]
    if data.empty:
        return None

    return (
        data.groupby("ticker")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )
