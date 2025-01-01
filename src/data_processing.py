"""Data loading and preprocessing functions."""

from typing import Union, Tuple
import pandas as pd
from sklearn.model_selection import train_test_split

from .config import DATA_CONFIG


def load_data(file_path: str) -> pd.DataFrame:
    """Load data from CSV or Parquet file.
    
    Args:
        file_path: Path to the data file
        
    Returns:
        Loaded DataFrame
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.parquet'):
        return pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Parquet.")


def preprocess_data(
    df: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Preprocess the data and split into features and target.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Tuple of (features, target)
    """
    X = df.drop(columns=[DATA_CONFIG["target_column"]])
    y = df[DATA_CONFIG["target_column"]]
    
    return X, y


def split_data(
    X: pd.DataFrame,
    y: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and test sets.
    
    Args:
        X: Feature DataFrame
        y: Target Series
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X, y,
        test_size=DATA_CONFIG["test_size"],
        random_state=DATA_CONFIG["random_state"]
    )
