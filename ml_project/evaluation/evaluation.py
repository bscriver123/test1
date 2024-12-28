# Dummy evaluation script
from sklearn.metrics import accuracy_score

def evaluate_model(model, test_data, test_labels):
    predictions = model.predict(test_data)
    return accuracy_score(test_labels, predictions)
