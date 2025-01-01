"""Tests for data processing functions."""

import pytest
import pandas as pd
from src.data_processing import load_data, preprocess_data


def test_load_data_csv(tmp_path):
    """Test loading CSV data."""
    df = pd.DataFrame({"a": [1, 2], "target": [0, 1]})
    csv_path = tmp_path / "test.csv"
    df.to_csv(csv_path, index=False)
    
    loaded_df = load_data(str(csv_path))
    assert isinstance(loaded_df, pd.DataFrame)
    assert loaded_df.shape == (2, 2)


def test_preprocess_data():
    """Test data preprocessing."""
    df = pd.DataFrame({
        "feature1": [1, 2],
        "feature2": [3, 4],
        "target": [0, 1]
    })
    
    X, y = preprocess_data(df)
    assert X.shape == (2, 2)
    assert y.shape == (2,)
