# ==========================================================
# Exploratory Data Analysis Utilities for Solar Challenge
# ==========================================================

"""
eda_tools.py
Reusable helper functions for exploratory data analysis (EDA).
Author: Rufta Gaiem Weldegiorgis
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)


# ----------------------------------------------------------
# 📈 1. Time-Series Plots
# ----------------------------------------------------------
def plot_daily_ghi(df: pd.DataFrame, country: str):
    """Plot daily average GHI for a given country."""
    df_daily = df.resample('D').mean(numeric_only=True)
    plt.figure(figsize=(14,5))
    plt.plot(df_daily.index, df_daily['GHI'], color='orange', linewidth=1)
    plt.title(f"Daily Average GHI - {country}")
    plt.xlabel("Date")
    plt.ylabel("GHI (W/m²)")
    plt.show()


# ----------------------------------------------------------
# 🔥 2. Correlation Heatmap
# ----------------------------------------------------------
def plot_correlation_heatmap(df: pd.DataFrame, cols: list, title: str = "Correlation Heatmap"):
    """Generate correlation heatmap for selected columns."""
    corr_df = df[cols].dropna()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title(title)
    plt.show()


# ----------------------------------------------------------
# ⚡ 3. Scatter Plot
# ----------------------------------------------------------
def plot_scatter(df: pd.DataFrame, x: str, y: str, color='blue', alpha=0.5, title=None):
    """Generate a scatter plot for two numeric variables."""
    plt.figure(figsize=(10,5))
    sns.scatterplot(x=x, y=y, data=df, alpha=alpha, color=color)
    plt.title(title or f"{x} vs {y}")
    plt.show()


# ----------------------------------------------------------
# 🌬️ 4. Wind Speed Histogram
# ----------------------------------------------------------
def plot_wind_histogram(df: pd.DataFrame):
    """Plot histogram of wind speed (WS)."""
    plt.figure(figsize=(8,4))
    df['WS'].dropna().hist(bins=30)
    plt.title('Wind Speed Distribution')
    plt.xlabel('WS (m/s)')
    plt.ylabel('Frequency')
    plt.show()


# ----------------------------------------------------------
# 💧 5. Bubble Chart (Humidity–Temperature–GHI)
# ----------------------------------------------------------
def plot_bubble_chart(df: pd.DataFrame):
    """Plot bubble chart: Temperature vs GHI (bubble size = RH)."""
    plt.figure(figsize=(10,6))
    plt.scatter(
        df['Tamb'],
        df['GHI'],
        s=df['RH'], # bubble size = humidity
        alpha=0.4,
        c=df['RH'],
        cmap='coolwarm'
    )
    plt.title('Bubble Chart: GHI vs Tamb (bubble size = RH)')
    plt.xlabel('Temperature (Tamb)')
    plt.ylabel('GHI (W/m²)')
    plt.colorbar(label='Relative Humidity (%)')
    plt.show()


# ----------------------------------------------------------
# 🧼 6. Cleaning Impact Comparison
# ----------------------------------------------------------
def compare_cleaning_effect(df: pd.DataFrame):
    """Compare ModA and ModB averages before vs after cleaning."""
    if 'Cleaning' not in df.columns:
        print("⚠️ No Cleaning column found.")
        return

    before = df[df['Cleaning'] == 0][['ModA','ModB']].mean()
    after = df[df['Cleaning'] == 1][['ModA','ModB']].mean()

    print("Average before cleaning:\n", before)
    print("\nAverage after cleaning:\n", after)
    print("\nChange (after - before):\n", after - before)