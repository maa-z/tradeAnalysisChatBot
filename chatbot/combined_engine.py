def trade_vs_performance(trades_df, holdings_df):
    trade_counts = (
        trades_df.groupby("portfolioname")
        .size()
        .rename("total_trades")
    )

    performance = (
        holdings_df.groupby("portfolioname")["pl_ytd"]
        .sum()
        .rename("pl_ytd")
    )

    return trade_counts.to_frame().join(performance, how="inner")
