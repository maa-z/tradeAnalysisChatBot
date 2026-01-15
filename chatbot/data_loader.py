import pandas as pd
from chatbot.data_cleaning import clean_holdings, clean_trades

def load_data():
    holdings = pd.read_csv("data/holdings.csv")
    trades = pd.read_csv("data/trades.csv")

    holdings = clean_holdings(holdings)
    trades = clean_trades(trades)

    return holdings, trades
