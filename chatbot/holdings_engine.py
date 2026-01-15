def total_holdings(df, fund):
    data = df[
        (df["portfolioname"].str.lower() == fund.lower()) &
        (df["qty"] > 0) &
        (df["closedate"].isna())
    ]
    return len(data)


def fund_performance(df):
    perf = (
        df.groupby("portfolioname")["pl_ytd"]
        .sum()
        .sort_values(ascending=False)
    )
    return perf



def count_holdings(df, fund):
    data = df[
        (df["portfolioname"] == fund) &
        (df["qty"] > 0) &
        (df["closedate"].isna())
    ]
    return len(data)


def performance_by_fund(df):
    return (
        df.groupby("portfolioname")["pl_ytd"]
        .sum()
        .sort_values(ascending=False)
    )


def funds_holding_security(df, security):
    data = df[df["secname"] == security]
    return sorted(data["portfolioname"].unique())
