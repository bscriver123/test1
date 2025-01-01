"""Feature engineering functions."""

from typing import List
import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_features(
    df: pd.DataFrame,
    columns: List[str]
) -> pd.DataFrame:
    """Scale numerical features.
    
    Args:
        df: Input DataFrame
        columns: List of columns to scale
        
    Returns:
        DataFrame with scaled features
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create new features from existing ones.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with new features
    """
    # Add feature engineering logic here
    return df
