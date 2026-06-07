"""XGBoost risk prediction model wrapper."""
import joblib
import pandas as pd
import xgboost as xgb
from typing import Optional, Dict, Any
from pathlib import Path


class RiskModel:
    """Risk prediction model for street segments."""
    
    def __init__(self, params: Optional[Dict[str, Any]] = None):
        self.params = params or {
            'objective': 'multi:softprob',
            'num_class': 5,
            'max_depth': 6,
            'learning_rate': 0.1,
            'n_estimators': 100,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'min_child_weight': 3,
            'gamma': 0.1,
            'random_state': 42,
            'n_jobs': -1
        }
        self.model = None
        self.feature_names = None
    
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> Dict[str, float]:
        self.feature_names = X_train.columns.tolist()
        
        print(f"Training XGBoost with {len(X_train)} samples, {len(self.feature_names)} features")
        
        self.model = xgb.XGBClassifier(**self.params)
        self.model.fit(X_train, y_train)
        
        train_pred = self.model.predict(X_train)
        from sklearn.metrics import f1_score
        train_f1 = f1_score(y_train, train_pred, average='macro')
        
        print(f"✅ Training complete. F1: {train_f1:.4f}")
        
        return {'train_f1': train_f1}
    
    def predict(self, X: pd.DataFrame):
        if self.model is None:
            raise ValueError("Model not trained yet!")
        return self.model.predict(X)
    
    def predict_proba(self, X: pd.DataFrame):
        if self.model is None:
            raise ValueError("Model not trained yet!")
        return self.model.predict_proba(X)
    
    def save(self, path: str):
        joblib.dump({'model': self.model, 'feature_names': self.feature_names, 'params': self.params}, path)
        print(f"✅ Model saved to {path}")
    
    def load(self, path: str):
        data = joblib.load(path)
        self.model = data['model']
        self.feature_names = data['feature_names']
        self.params = data['params']
        print(f"✅ Model loaded from {path}")
