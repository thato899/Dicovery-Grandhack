import joblib
import pandas as pd
import numpy as np

class RiskPredictor:
    def __init__(self, model_path='risk_model.pkl'):
        data = joblib.load(model_path)
        self.model = data['model'] if isinstance(data, dict) else data
        self.feature_names = data.get('feature_names', None) if isinstance(data, dict) else None
    
    def predict(self, features):
        """Predict risk from feature array"""
        if isinstance(features, dict):
            df = pd.DataFrame([features])
            return self.model.predict(df)[0]
        else:
            return self.model.predict(features.reshape(1, -1))[0]
    
    def predict_proba(self, features):
        """Get probability distribution"""
        if isinstance(features, dict):
            df = pd.DataFrame([features])
            return self.model.predict_proba(df)[0]
        else:
            return self.model.predict_proba(features.reshape(1, -1))[0]

print("✅ RiskPredictor wrapper created")
