# ai_core/ensemble.py
from inference import predict_signal

def ensemble_predict(data):
    # Future: combine multiple models (LSTM, RF, etc.)
    # For now, just call logistic regression
    return predict_signal(data)
