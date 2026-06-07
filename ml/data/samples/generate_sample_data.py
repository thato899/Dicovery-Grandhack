"""Generate sample datasets for testing and development."""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_crime_samples(n: int = 1000) -> pd.DataFrame:
    """Generate synthetic crime data."""
    np.random.seed(42)
    
    # Johannesburg CBD approximate bounds
    lats = np.random.uniform(-26.25, -26.15, n)
    lons = np.random.uniform(28.00, 28.08, n)
    
    crime_types = ['robbery', 'assault', 'theft', 'burglary', 'murder', 'carjacking']
    severities = ['low', 'medium', 'high', 'critical']
    severity_weights = [0.2, 0.4, 0.3, 0.1]
    
    start_date = datetime(2025, 1, 1)
    dates = [start_date + timedelta(days=random.randint(0, 500)) for _ in range(n)]
    
    return pd.DataFrame({
        'latitude': lats,
        'longitude': lons,
        'crime_type': np.random.choice(crime_types, n),
        'severity': np.random.choice(severities, n, p=severity_weights),
        'timestamp': dates,
        'area_name': ['Johannesburg CBD'] * n
    })

def generate_report_samples(n: int = 500) -> pd.DataFrame:
    """Generate synthetic community report data."""
    np.random.seed(42)
    
    lats = np.random.uniform(-26.25, -26.15, n)
    lons = np.random.uniform(28.00, 28.08, n)
    report_types = ['dangerous_area', 'suspicious_activity', 'lighting_issue', 'unsafe_condition', 'safe_area']
    risk_levels = np.random.randint(0, 6, n)
    
    start_date = datetime(2025, 6, 1)
    dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(n)]
    
    return pd.DataFrame({
        'latitude': lats,
        'longitude': lons,
        'report_type': np.random.choice(report_types, n),
        'risk_level': risk_levels,
        'timestamp': dates
    })

def generate_environmental_samples(n: int = 10000) -> pd.DataFrame:
    """Generate synthetic environmental data."""
    np.random.seed(42)
    
    lats = np.random.uniform(-26.25, -26.15, n)
    lons = np.random.uniform(28.00, 28.08, n)
    
    lighting_scores = np.random.beta(2, 2, n)
    crowd_densities = np.random.beta(1.5, 3, n)
    
    weather_conditions = ['clear', 'rain', 'fog', 'storm']
    weather_probs = [0.7, 0.15, 0.1, 0.05]
    
    days = np.random.randint(0, 7, n)
    hours = np.random.choice(range(24), n)
    
    start_date = datetime(2025, 6, 1)
    dates = [start_date + timedelta(hours=random.randint(0, 24*365)) for _ in range(n)]
    
    return pd.DataFrame({
        'latitude': lats,
        'longitude': lons,
        'street_lighting_score': lighting_scores,
        'crowd_density': crowd_densities,
        'weather': np.random.choice(weather_conditions, n, p=weather_probs),
        'day_of_week': days,
        'hour_of_day': hours,
        'timestamp': dates
    })

if __name__ == "__main__":
    # Create raw directory if it doesn't exist
    os.makedirs('../raw', exist_ok=True)
    
    # Generate and save
    print("Generating crime samples...")
    crime_df = generate_crime_samples(1000)
    crime_df.to_csv('../raw/crime_data.csv', index=False)
    print(f"  ✓ Saved 1000 crime records")
    
    print("Generating community reports...")
    reports_df = generate_report_samples(500)
    reports_df.to_csv('../raw/community_reports.csv', index=False)
    print(f"  ✓ Saved 500 community reports")
    
    print("Generating environmental data...")
    env_df = generate_environmental_samples(10000)
    env_df.to_csv('../raw/environmental_data.csv', index=False)
    print(f"  ✓ Saved 10000 environmental records")
    
    print("\n✅ Sample data generated successfully!")
