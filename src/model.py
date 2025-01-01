"""XGBoost model training and prediction."""

from typing import Any
import pandas as pd
import xgboost as xgb

from .config import MODEL_CONFIG


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series
) -> xgb.XGBRegressor:
    """Train XGBoost model.
    
    Args:
        X_train: Training features
        y_train: Training targets
        
    Returns:
        Trained model
    """
    model = xgb.XGBRegressor(**MODEL_CONFIG)
    model.fit(X_train, y_train)
    return model


def predict(
    model: xgb.XGBRegressor,
    X: pd.DataFrame
) -> pd.Series:
    """Make predictions using trained model.
    
    Args:
        model: Trained XGBoost model
        X: Features to predict on
        
    Returns:
        Predictions
    """
    return model.predict(X)
