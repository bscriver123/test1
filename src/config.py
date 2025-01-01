"""Configuration parameters for the ML project."""

from typing import Dict, Any

# Data processing config
DATA_CONFIG: Dict[str, Any] = {
    "random_state": 42,
    "test_size": 0.2,
    "target_column": "target"
}

# Model parameters
MODEL_CONFIG: Dict[str, Any] = {
    "max_depth": 6,
    "learning_rate": 0.1,
    "n_estimators": 100,
    "objective": "reg:squarederror"
}
