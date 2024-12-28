# Dummy modeling script
import xgboost as xgb

def train_model(data, labels):
    model = xgb.XGBClassifier()
    model.fit(data, labels)
    return model
