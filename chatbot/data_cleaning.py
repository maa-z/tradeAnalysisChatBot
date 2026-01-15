# import pandas as pd

# def clean_holdings(df: pd.DataFrame) -> pd.DataFrame:
#     df = df.copy()

#     df.columns = [c.strip().lower() for c in df.columns]

#     date_cols = ["asofdate", "opendate", "closedate"]
#     for col in date_cols:
#         df[col] = pd.to_datetime(df[col], errors="coerce")

#     numeric_cols = [
#         "qty", "startqty", "mv_local", "mv_base",
#         "pl_dtd", "pl_mtd", "pl_qtd", "pl_ytd"
#     ]
#     for col in numeric_cols:
#         df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

#     df["portfolioname"] = df["portfolioname"].str.strip()
#     df["secname"] = df["secname"].str.strip()

#     return df


# def clean_trades(df: pd.DataFrame) -> pd.DataFrame:
#     df = df.copy()

#     df.columns = [c.strip().lower() for c in df.columns]

#     numeric_cols = [
#         "quantity", "price", "principal",
#         "totalcash", "allocationqty", "allocationcash"
#     ]
#     for col in numeric_cols:
#         df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

#     df["tradetypename"] = df["tradetypename"].str.lower()
#     df["portfolioname"] = df["portfolioname"].str.strip()
#     df["ticker"] = df["ticker"].astype(str).str.strip()

#     return df













import pandas as pd

def clean_holdings(df):
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]

    # Explicit date parsing (fixes warning)
    for col in ["asofdate", "opendate", "closedate"]:
        df[col] = pd.to_datetime(
            df[col],
            format="%m/%d/%Y",
            errors="coerce"
        )

    numeric_cols = [
        "qty", "startqty", "mv_local", "mv_base",
        "pl_dtd", "pl_mtd", "pl_qtd", "pl_ytd"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["portfolioname"] = df["portfolioname"].str.strip().str.lower()
    df["secname"] = df["secname"].str.strip().str.upper()

    return df


def clean_trades(df):
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]

    numeric_cols = [
        "quantity", "price", "principal",
        "totalcash", "allocationqty", "allocationcash"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["portfolioname"] = df["portfolioname"].str.strip().str.lower()
    df["ticker"] = df["ticker"].astype(str).str.strip().str.upper()
    df["tradetypename"] = df["tradetypename"].str.lower()

    return df
