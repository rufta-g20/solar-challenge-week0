from scripts.clean_data import load_and_basic_clean
import pandas as pd
import os

def test_load_and_basic_clean():
    test_file = "data/benin-malanville.csv"
    df = load_and_basic_clean(test_file, "Benin")
    assert 'Country' in df.columns
    assert not df.index.duplicated().any()
    assert (df[['GHI','DNI','DHI']] >= 0).all().all()