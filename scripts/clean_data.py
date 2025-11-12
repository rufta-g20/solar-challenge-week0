# scripts/clean_data.py
import pandas as pd
import numpy as np
from scipy import stats

def load_and_basic_clean(file_path: str, country_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df = df.set_index('Timestamp').sort_index()
    else:
        raise ValueError(f"'Timestamp' column missing in {file_path}")

    # Remove exact duplicate rows (same timestamp and same data)
    df = df[~df.index.duplicated(keep='first')]

    # Clip irradiance to non-negative values
    for col in ['GHI','DNI','DHI']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').clip(lower=0)

    df['Country'] = country_name
    return df

def flag_zscore_outliers(df: pd.DataFrame, cols):
    """Return DataFrame with new boolean columns <col>_z_outlier True where |z|>3"""
    outlier_flags = pd.DataFrame(index=df.index)
    for col in cols:
        if col in df.columns:
            # compute zscore ignoring NaNs
            z = np.abs(stats.zscore(df[col].dropna()))
            # align z back to index
            z_full = pd.Series(index=df[col].dropna().index, data=z)
            flag = df[col].index.to_series().apply(lambda idx: bool(z_full.get(idx, False)))
            outlier_flags[f"{col}_z_outlier"] = flag
    return pd.concat([df, outlier_flags], axis=1)

def impute_median(df: pd.DataFrame, cols):
    for col in cols:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df

def export_clean(df: pd.DataFrame, out_path: str):
    # save cleaned csv locally (do not commit)
    df.to_csv(out_path, index=True)