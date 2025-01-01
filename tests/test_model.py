"""Unit tests for model functionality."""

import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import make_regression

from src.data_processing import load_data, preprocess_data, split_data
from src.model import train_model, predict
from src.evaluation import evaluate_model


@pytest.fixture
def sample_data():
    """Create sample regression dataset."""
    X, y = make_regression(
        n_samples=100,
        n_features=5,
        random_state=42
    )
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
    df["target"] = y
    return df


def test_model_training(sample_data):
    """Test full model training pipeline."""
    # Preprocess data
    X, y = preprocess_data(sample_data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train model
    model = train_model(X_train, y_train)
    assert model is not None
    
    # Make predictions
    y_pred = predict(model, X_test)
    assert len(y_pred) == len(y_test)
    
    # Evaluate model
    metrics = evaluate_model(y_test, y_pred)
    assert "rmse" in metrics
    assert "mae" in metrics
    assert "r2" in metrics
    assert metrics["r2"] > 0  # Should be better than random for this simple dataset


def test_data_loading(tmp_path):
    """Test data loading functionality."""
    # Create a temporary CSV file
    df = pd.DataFrame({
        "feature_1": [1, 2, 3],
        "target": [0.5, 1.0, 1.5]
    })
    csv_path = tmp_path / "test.csv"
    parquet_path = tmp_path / "test.parquet"
    
    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)
    
    # Test CSV loading
    df_csv = load_data(str(csv_path))
    assert isinstance(df_csv, pd.DataFrame)
    assert len(df_csv) == 3
    
    # Test Parquet loading
    df_parquet = load_data(str(parquet_path))
    assert isinstance(df_parquet, pd.DataFrame)
    assert len(df_parquet) == 3
    
    # Test unsupported format
    with pytest.raises(ValueError):
        load_data("invalid.txt")
