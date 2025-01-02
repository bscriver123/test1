"""
Evaluation module for model assessment and metrics calculation.
"""
from typing import Dict, Union, Optional
import numpy as np
from loguru import logger
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    mean_absolute_error
)


def mean_absolute_percentage_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate Mean Absolute Percentage Error (MAPE).
    
    Args:
        y_true: True values
        y_pred: Predicted values
        
    Returns:
        float: MAPE value
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    non_zero_mask = y_true != 0
    return np.mean(np.abs((y_true[non_zero_mask] - y_pred[non_zero_mask]) / y_true[non_zero_mask])) * 100


class Evaluator:
    """A class to evaluate model performance using various metrics."""

    def __init__(self, metrics: Optional[list] = None):
        """
        Initialize the Evaluator.

        Args:
            metrics: List of metric names to calculate
        """
        self.metrics = metrics or ['accuracy', 'precision', 'recall', 'f1', 'roc_auc', 'mae', 'mape']

    def calculate_metrics(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_prob: Optional[np.ndarray] = None
    ) -> Dict[str, float]:
        """
        Calculate specified evaluation metrics.

        Args:
            y_true: True labels
            y_pred: Predicted labels
            y_prob: Predicted probabilities (for ROC-AUC)

        Returns:
            Dict[str, float]: Dictionary of metric names and values

        Raises:
            ValueError: If inputs are invalid or incompatible
        """
        try:
            results = {}
            
            if 'accuracy' in self.metrics:
                results['accuracy'] = accuracy_score(y_true, y_pred)
            
            if 'precision' in self.metrics:
                results['precision'] = precision_score(y_true, y_pred)
            
            if 'recall' in self.metrics:
                results['recall'] = recall_score(y_true, y_pred)
            
            if 'f1' in self.metrics:
                results['f1'] = f1_score(y_true, y_pred)
            
            if 'roc_auc' in self.metrics and y_prob is not None:
                results['roc_auc'] = roc_auc_score(y_true, y_prob)
            
            if 'mae' in self.metrics:
                results['mae'] = mean_absolute_error(y_true, y_pred)
            
            if 'mape' in self.metrics:
                results['mape'] = mean_absolute_percentage_error(y_true, y_pred)

            return results

        except Exception as e:
            raise ValueError(f"Error calculating metrics: {str(e)}")
