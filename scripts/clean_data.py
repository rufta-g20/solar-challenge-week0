"""
clean_data.py
Reusable data cleaning functions for solar farm datasets.
Author: Rufta Gaiem Weldegiorgis
"""

import pandas as pd
import numpy as np
from scipy import stats


# ----------------------------------------------------------
# 🧹 1. Load and Basic Clean
# ----------------------------------------------------------
def load_and_basic_clean(file_path: str, country_name: str) -> pd.DataFrame:
    """
    Load a solar dataset, set Timestamp index, remove duplicates,
    and clip irradiance values to non-negative.
    """
    df = pd.read_csv(file_path)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df = df.set_index('Timestamp').sort_index()
    else:
        raise ValueError(f"'Timestamp' column missing in {file_path}")

    # Remove exact duplicate rows (same timestamp & data)
    df = df[~df.index.duplicated(keep='first')]

    # Clip irradiance to non-negative values
    for col in ['GHI', 'DNI', 'DHI']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').clip(lower=0)

    df['Country'] = country_name
    return df


# ----------------------------------------------------------
# ⚠️ 2. Flag Z-Score Outliers
# ----------------------------------------------------------
def flag_zscore_outliers(df: pd.DataFrame, cols):
    """Return DataFrame with new boolean columns <col>_z_outlier True where |Z|>3."""
    outlier_flags = pd.DataFrame(index=df.index)
    for col in cols:
        if col in df.columns:
            z = np.abs(stats.zscore(df[col].dropna()))
            z_full = pd.Series(index=df[col].dropna().index, data=z)
            flag = df[col].index.to_series().apply(lambda idx: bool(z_full.get(idx, False)))
            outlier_flags[f"{col}_z_outlier"] = flag

    return pd.concat([df, outlier_flags], axis=1)


# ----------------------------------------------------------
# 🧮 3. Median Imputation
# ----------------------------------------------------------
def impute_median(df: pd.DataFrame, cols):
    """Fill missing values in specified columns using the median."""
    for col in cols:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df


# ----------------------------------------------------------
# 💾 4. Export Cleaned Data
# ----------------------------------------------------------
def export_clean(df: pd.DataFrame, out_path: str):
    """Save cleaned CSV locally (do not commit to Git)."""
    df.to_csv(out_path, index=True)
    print(f"✅ Cleaned data exported to: {out_path}")


# ----------------------------------------------------------
# 📊 5. Summarize Outliers (Improved Version)
# ----------------------------------------------------------
def summarize_outliers(df: pd.DataFrame, cols):
    """
    Compute and summarize Z-score outliers for selected columns.
    Adds <col>_z_outlier flags and 'any_z_outlier' summary column.
    Prints total flagged counts per metric and overall.
    """
    outlier_flags = pd.DataFrame(index=df.index)

    for col in cols:
        if col in df.columns:
            z = np.abs(stats.zscore(df[col].dropna()))
            z_full = pd.Series(index=df[col].dropna().index, data=z)
            flag = df[col].index.to_series().apply(lambda idx: bool(z_full.get(idx, False)))
            outlier_flags[f"{col}_z_outlier"] = flag
            print(f"{col}: {flag.sum()} rows flagged as outliers (|Z|>3)")

    df_flagged = pd.concat([df, outlier_flags], axis=1)
    df_flagged["any_z_outlier"] = df_flagged[[c for c in outlier_flags.columns]].any(axis=1)

    print("\nTotal rows flagged as outlier for any metric:",
          df_flagged["any_z_outlier"].sum())

    return df_flagged