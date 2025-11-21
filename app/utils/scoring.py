import pandas as pd

def apply_role_score(df: pd.DataFrame, role_key: str, weights: dict, weight_version: str = "Default") -> pd.DataFrame:
    """
    Apply weights for a role and add a normalized `score` column (0-100).

    weights: dict loaded from weights.json
    role_key: key in weights (e.g. 'ST', 'MC', 'DC')
    weight_version: usually 'Default' unless you provide multiple versions per role
    """
    df = df.copy()
    role_def = weights.get(role_key)
    if role_def is None:
        raise KeyError(f"Role {role_key} not found in weights.json")
    
    role_weights = role_def[weight_version]
    if role_weights is None:
        raise KeyError(f"Weight version {weight_version} for role {role_key} not found")

    # score = Σ(attribute × weight)
    attr_cols = [a for a in role_weights.keys() if a in df.columns]
    if not attr_cols:
        df['score_raw'] = 0
    else:
        df["score_raw"] = sum(
            df[attr] * weight
            for attr, weight in role_weights.items()
            if attr in df.columns
        )

    # normalize 0–100 for UI
    minv = df['score_raw'].min()
    maxv = df['score_raw'].max()
    if maxv - minv == 0:
        df['score'] = 0
    else:
        df['score'] = 100 * (df['score_raw'] - minv) / (maxv - minv)

    return df
