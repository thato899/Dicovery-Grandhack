"""Temporal feature engineering for time-based risk patterns."""
import numpy as np
from datetime import datetime


class TemporalFeatureEngineer:
    """Engineer temporal features for risk prediction."""
    
    @staticmethod
    def create_time_features(dt: datetime) -> dict:
        hour_rad = 2 * np.pi * dt.hour / 24
        hour_sin = np.sin(hour_rad)
        hour_cos = np.cos(hour_rad)
        
        dow_rad = 2 * np.pi * dt.weekday() / 7
        dow_sin = np.sin(dow_rad)
        dow_cos = np.cos(dow_rad)
        
        month_rad = 2 * np.pi * dt.month / 12
        month_sin = np.sin(month_rad)
        month_cos = np.cos(month_rad)
        
        is_weekend = 1.0 if dt.weekday() >= 5 else 0.0
        is_nighttime = 1.0 if dt.hour < 6 or dt.hour >= 20 else 0.0
        is_rush_hour = 1.0 if (7 <= dt.hour <= 9) or (16 <= dt.hour <= 18) else 0.0
        
        return {
            'hour_sin': hour_sin,
            'hour_cos': hour_cos,
            'day_of_week_sin': dow_sin,
            'day_of_week_cos': dow_cos,
            'month_sin': month_sin,
            'month_cos': month_cos,
            'is_weekend': is_weekend,
            'is_nighttime': is_nighttime,
            'is_rush_hour': is_rush_hour,
        }
