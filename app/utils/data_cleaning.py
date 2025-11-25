import pandas as pd
import numpy as np
import re

attributes = [
    "acc", "aer", "agg", "agi", "ant", "bal", "bra", "cmd", "com", "cmp", "cnt", "cor", "cro",
    "dec", "det", "dri", "ecc", "fin", "fir", "fla", "fre", "han", "hea", "jum", "kic", "ldr",
    "lon", "l_th", "mar", "nat", "otb", "1v1", "pac", "pas", "pen", "pos", "pun", "ref", "tro",
    "sta", "str", "tck", "tea", "tec", "thr", "vis", "wor"
]


def parse_value_range(value_str):
    """
    Parse Football Manager transfer value strings into min/max numeric values (GBP).
    
    Examples:
    ----------
    £54M - £67M → (54000000.0, 67000000.0)
    £45M → (45000000.0, 45000000.0)
    Not for Sale → (500000000.0, 500000000.0)
    Unknown → (NaN, NaN)
    """
    if not isinstance(value_str, str) or value_str.strip() == (""):
        return (np.nan, np.nan)
    
    value_str = value_str.strip()

    # Handle 'Not for sale'
    if value_str.lower() == 'not for sale':
        return (500_000_000.0, 500_000_000.0)
    
    # Handle Unknown or Loan or Free Transfer
    if value_str.lower() == 'unknown':
        return (np.nan, np.nan)
    
    # Handle ranges like "£54M - £67M"
    if "-" in value_str:
        parts = [p.strip() for p in value_str.split('-')]
        values = [parse_value_range(p)[0] for p in parts]
        if len(values) == 2:
            return (min(values), max(values))
        else:
            return (values[0], values[0]) if values else (np.nan, np.nan)
    
    # Extract numeric value with suffix
    match = re.search(r"£([\d\.]+)([KMB]?)", value_str)
    if not match:
        return (np.nan, np.nan)
    
    num = float(match.group(1))
    suffix = match.group(2)
    multiplier = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000, "": 1}

    value = num * multiplier.get(suffix, 1)
    
    return (value, value)

def get_att_value(value):
    if isinstance(value, str) and '-' in value:
        low, high = map(float, value.split('-'))
        return (low + high) / 2
    return value


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Uniform column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Drop the first row which have all null values
    df = df.dropna(how='all')

    # remove duplicates
    df = df.drop_duplicates()

    cols_to_rename = {'nat':'nation', 'nat.1':'nat', 'salary':'wages' }
    df.rename(columns=cols_to_rename, inplace=True)

    df.replace('-', np.nan, inplace=True)

    # Remove units from height, weight and wages
    df['height'] = df['height'].str.extract(r'(\d+)')
    df['weight'] = df['weight'].str.extract(r'(\d+)')
    df['wages'] = df['wages'].str.replace('[£, p/w]', '', regex=True)
    df[['height','weight','wages']] = df[['height','weight','wages']].apply(pd.to_numeric, errors='coerce')

    df['expires'] = pd.to_datetime(df['expires'], format='%m/%d/%Y', errors='coerce')

    # Add feet feature
    foot_values = {
        'Very Strong' : 10,
        'Fairly Strong' : 8,
        'Strong' : 6,
        'Reasonable' : 4,
        'Weak': 2,
        'Very Weak' : 0
    }

    df[['left_foot', 'right_foot']] = df[['left_foot', 'right_foot']].fillna('Very Weak')

    df['lf_val'] = df['left_foot'].apply(lambda x: foot_values[x])
    df['rf_val'] = df['right_foot'].apply(lambda x: foot_values[x])

    df[['lf_val', 'rf_val']] =  df[['lf_val', 'rf_val']].apply(pd.to_numeric, errors='coerce')

    df['feet'] = df['lf_val'] + df['rf_val']
    df['feet'] =df['feet'].apply(pd.to_numeric, errors='coerce')

    # spliting the transfer value into min and max value
    value_ranges = df['transfer_value'].apply(parse_value_range)

    df['min_value'] = value_ranges.apply(lambda x: x[0])
    df['max_value'] = value_ranges.apply(lambda x: x[1])

    for col in attributes:
        df[col] = df[col].apply(get_att_value)
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df.groupby('best_pos')[col].transform(lambda x: x.fillna(round(x.mean(),2)))

    # only keep desire columns
    cols_to_keep = ['name', 'position', 'best_pos', 'age', 'nation', 'height', 'weight', 'club', 'transfer_value', 'min_value', 'max_value', 'wages', 'expires', 'division', 'style', 'feet'] + attributes

    return df[cols_to_keep]