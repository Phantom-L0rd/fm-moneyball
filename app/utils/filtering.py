import pandas as pd


def filter_by_budget(df: pd.DataFrame, max_million: float) -> pd.DataFrame:
    # assume value_min is in GBP (raw), so convert to millions if needed
    # if your df stores in GBP integer, use /1e6
    df = df.copy()
    if 'min_value' in df.columns:
        try:
            df = df[df['min_value'] <= max_million * 1_000_000]
        except Exception:
            # try comparing to million scale already
            df = df[df['min_value'] <= max_million]
    return df


