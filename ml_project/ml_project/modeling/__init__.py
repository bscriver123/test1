"""
Modeling module for training models and making predictions.
"""
from typing import Optional, Union, Dict, Any
import numpy as np
import xgboost as xgb
from sklearn.base import BaseEstimator
from loguru import logger


class XGBoostModel:
    """A wrapper class for XGBoost model."""

    def __init__(self, params: Optional[Dict[str, Any]] = None):
        """
        Initialize the XGBoost model.

        Args:
            params: Dictionary of model parameters
        """
        self.params = params or {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss'
        }
        self.model = None

    def train(
        self, 
        X_train: Union[np.ndarray, xgb.DMatrix],
        y_train: Optional[np.ndarray] = None,
        **kwargs
    ) -> BaseEstimator:
        """
        Train the XGBoost model.

        Args:
            X_train: Training features
            y_train: Training labels
            **kwargs: Additional training parameters

        Returns:
            BaseEstimator: Trained model

        Raises:
            ValueError: If input data is invalid
        """
        try:
            if not isinstance(X_train, xgb.DMatrix):
                dtrain = xgb.DMatrix(X_train, label=y_train)
            else:
                dtrain = X_train

            self.model = xgb.train(self.params, dtrain, **kwargs)
            return self.model

        except Exception as e:
            raise ValueError(f"Error during model training: {str(e)}")

    def predict(self, X: Union[np.ndarray, xgb.DMatrix]) -> np.ndarray:
        """
        Make predictions using the trained model.

        Args:
            X: Features to make predictions on

        Returns:
            np.ndarray: Predicted values

        Raises:
            ValueError: If model is not trained or input is invalid
        """
        if self.model is None:
            raise ValueError("Model must be trained before making predictions")

        try:
            if not isinstance(X, xgb.DMatrix):
                dtest = xgb.DMatrix(X)
            else:
                dtest = X
            return self.model.predict(dtest)

        except Exception as e:
            raise ValueError(f"Error during prediction: {str(e)}")
