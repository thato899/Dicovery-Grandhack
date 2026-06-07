import joblib
import numpy as np
import pandas as pd

# Load model
print("Loading model...")
model_data = joblib.load('models/production/risk_model.pkl')
model = model_data['model'] if isinstance(model_data, dict) else model_data
print(f"✅ Model loaded")

# Feature names (14 features)
feature_names = [
    'crime_density', 'crime_severity', 'hour_sin', 'hour_cos',
    'day_of_week_sin', 'day_of_week_cos', 'month_sin', 'month_cos',
    'is_weekend', 'is_nighttime', 'is_rush_hour', 'lighting_risk',
    'crowd_risk', 'weather_risk'
]

# Test prediction
test_data = pd.DataFrame([[
    2.5, 2.0, -0.5, 0.866, 0.0, 1.0, 0.5, 0.866, 0, 1, 0, 0.7, 0.4, 0.2
]], columns=feature_names)

risk_class = model.predict(test_data)[0]
risk_proba = model.predict_proba(test_data)[0]

risk_levels = ['Safe', 'Low Risk', 'Medium Risk', 'High Risk', 'Extreme Risk']

print("\n" + "="*50)
print("📍 Risk Prediction Test")
print("="*50)
print(f"🎯 Risk Class: {risk_class}")
print(f"📊 Risk Level: {risk_levels[risk_class] if risk_class < len(risk_levels) else 'Unknown'}")
print(f"📈 Confidence: {max(risk_proba)*100:.1f}%")
print("\n📊 Probabilities:")
for i, prob in enumerate(risk_proba[:5]):
    bar = "█" * int(prob * 30)
    print(f"   {risk_levels[i]:12s}: {prob*100:5.1f}% {bar}")
print("="*50)
