"""Complete feature engineering pipeline."""
import pandas as pd
from typing import Optional, List
from .crime_features import CrimeFeatureEngineer
from .temporal_features import TemporalFeatureEngineer
from .environmental_features import EnvironmentalFeatureEngineer


class FeaturePipeline:
    """End-to-end feature engineering pipeline."""
    
    def __init__(self, crime_df: Optional[pd.DataFrame] = None):
        self.crime_engineer = None
        self.temporal_engineer = TemporalFeatureEngineer()
        self.env_engineer = EnvironmentalFeatureEngineer()
        
        if crime_df is not None:
            self.fit(crime_df)
    
    def fit(self, crime_df: pd.DataFrame) -> 'FeaturePipeline':
        self.crime_engineer = CrimeFeatureEngineer(radius_meters=500)
        self.crime_engineer.fit(crime_df)
        return self
    
    def transform(self, locations_df: pd.DataFrame) -> pd.DataFrame:
        if self.crime_engineer is None:
            raise ValueError("Pipeline must be fit before transform")
        
        features = []
        
        for idx, row in locations_df.iterrows():
            lat, lon = row['latitude'], row['longitude']
            dt = pd.to_datetime(row['timestamp'])
            
            crime_density = self.crime_engineer.calculate_crime_density(lat, lon)
            severity_score = self.crime_engineer.calculate_severity_score(lat, lon)
            time_features = self.temporal_engineer.create_time_features(dt)
            
            env_features = self.env_engineer.create_features({
                'street_lighting_score': row.get('street_lighting_score', 0.5),
                'crowd_density': row.get('crowd_density', 0.5),
                'weather': row.get('weather', 'clear'),
                'hour_of_day': dt.hour
            })
            
            feature_vector = {
                'crime_density': crime_density,
                'crime_severity': severity_score,
                **time_features,
                **env_features
            }
            features.append(feature_vector)
        
        return pd.DataFrame(features)
    
    def get_feature_names(self) -> List[str]:
        return [
            'crime_density', 'crime_severity',
            'hour_sin', 'hour_cos',
            'day_of_week_sin', 'day_of_week_cos',
            'month_sin', 'month_cos',
            'is_weekend', 'is_nighttime', 'is_rush_hour',
            'lighting_risk', 'crowd_risk', 'weather_risk'
        ]
