#!/usr/bin/env python
"""Training script for risk model."""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.features.pipeline import FeaturePipeline
from src.models.risk_model import RiskModel

def main():
    print("=" * 50)
    print("SafeRoute AI - Model Training")
    print("=" * 50)
    
    # Load crime data for feature engineering
    crime_df = pd.read_csv('data/raw/crime_data.csv')
    print(f"Loaded {len(crime_df)} crime records")
    
    # Load reports for labels
    reports_df = pd.read_csv('data/raw/community_reports.csv')
    reports_df['timestamp'] = pd.to_datetime(reports_df['timestamp'])
    print(f"Loaded {len(reports_df)} community reports")
    
    # Load environmental data
    env_df = pd.read_csv('data/raw/environmental_data.csv')
    env_df['timestamp'] = pd.to_datetime(env_df['timestamp'])
    print(f"Loaded {len(env_df)} environmental records")
    
    # Merge data (simplified - using reports as base)
    df = reports_df.copy()
    df = df.merge(
        env_df[['latitude', 'longitude', 'timestamp', 'street_lighting_score', 'crowd_density', 'weather']],
        on=['latitude', 'longitude', 'timestamp'],
        how='left'
    )
    
    # Fill missing values
    df['street_lighting_score'] = df['street_lighting_score'].fillna(0.5)
    df['crowd_density'] = df['crowd_density'].fillna(0.3)
    df['weather'] = df['weather'].fillna('clear')
    
    print(f"Prepared {len(df)} samples for training")
    
    # Create features
    print("\nEngineering features...")
    pipeline = FeaturePipeline(crime_df)
    X = pipeline.transform(df)
    y = df['risk_level']
    
    print(f"Created {X.shape[1]} features")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training: {len(X_train)} samples, Test: {len(X_test)} samples")
    
    # Train model
    print("\nTraining model...")
    model = RiskModel()
    metrics = model.train(X_train, y_train)
    
    # Evaluate
    from sklearn.metrics import classification_report, accuracy_score
    y_pred = model.predict(X_test)
    
    print("\n📊 Test Set Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs('models/production', exist_ok=True)
    model.save('models/production/risk_model.pkl')
    
    print("\n✅ Training complete!")

if __name__ == "__main__":
    main()
