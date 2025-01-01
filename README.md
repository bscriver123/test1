# ML Project

A machine learning project using XGBoost for prediction.

## Project Structure
```
src/
├── config.py           # Configuration parameters
├── data_processing.py  # Data loading and preprocessing
├── feature_engineering.py  # Feature engineering
├── model.py           # XGBoost model training
└── evaluation.py      # Model evaluation metrics
```

## Setup

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Run tests:
```bash
poetry run pytest
```

## Usage

```python
from src.data_processing import load_data
from src.model import train_model, predict

# Load and preprocess data
data = load_data("data.csv")

# Train model
model = train_model(data)

# Make predictions
predictions = predict(model, new_data)
```
