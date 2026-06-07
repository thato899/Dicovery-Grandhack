"""Crime density and risk feature engineering."""
import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree
from geopy.distance import geodesic


class CrimeFeatureEngineer:
    """Engineer features from crime data."""
    
    def __init__(self, radius_meters: float = 500.0):
        self.radius_meters = radius_meters
        self.ball_tree = None
        self.crime_coords = None
        self.crime_weights = None
    
    def fit(self, crime_df: pd.DataFrame) -> 'CrimeFeatureEngineer':
        """Fit BallTree on crime locations."""
        severity_weights = {'low': 1.0, 'medium': 2.0, 'high': 3.0, 'critical': 4.0}
        
        self.crime_coords = crime_df[['latitude', 'longitude']].values
        self.crime_weights = np.array([severity_weights.get(sev.lower(), 1.0) for sev in crime_df['severity']])
        
        # Convert to radians for haversine distance
        self.crime_coords_rad = np.radians(self.crime_coords)
        self.ball_tree = BallTree(self.crime_coords_rad, metric='haversine')
        return self
    
    def calculate_crime_density(self, lat: float, lon: float) -> float:
        """Calculate weighted crime density at a point."""
        point_rad = np.radians([[lat, lon]])
        radius_rad = self.radius_meters / 6371000  # Earth radius in meters
        
        indices = self.ball_tree.query_radius(point_rad, r=radius_rad)[0]
        
        if len(indices) == 0:
            return 0.0
        
        total_weight = np.sum(self.crime_weights[indices])
        area_km2 = np.pi * (self.radius_meters / 1000) ** 2
        density = total_weight / area_km2
        
        return min(density, 10.0)
    
    def calculate_severity_score(self, lat: float, lon: float) -> float:
        """Calculate average crime severity within radius."""
        point_rad = np.radians([[lat, lon]])
        radius_rad = self.radius_meters / 6371000
        
        indices = self.ball_tree.query_radius(point_rad, r=radius_rad)[0]
        
        if len(indices) == 0:
            return 1.0
        
        return float(np.mean(self.crime_weights[indices]))
    
    def distance_to_nearest_crime(self, lat: float, lon: float) -> float:
        """Calculate distance to nearest crime in meters."""
        point_rad = np.radians([[lat, lon]])
        
        distances, indices = self.ball_tree.query(point_rad, k=1)
        
        if len(distances[0]) == 0 or np.isnan(distances[0][0]):
            return 1000.0  # Default 1km if no crimes
        
        # Convert radians to meters
        distance_meters = distances[0][0] * 6371000
        return float(distance_meters)
