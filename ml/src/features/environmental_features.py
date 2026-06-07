"""Environmental feature engineering (lighting, crowd, weather)."""


class EnvironmentalFeatureEngineer:
    """Engineer environmental risk features."""
    
    @staticmethod
    def lighting_risk_score(lighting_score: float, hour: int) -> float:
        is_night = hour < 6 or hour >= 18
        night_boost = 2.0 if is_night else 1.0
        risk = (1 - lighting_score) * night_boost
        return min(risk, 1.0)
    
    @staticmethod
    def crowd_risk_score(crowd_density: float, hour: int) -> float:
        is_night = hour < 6 or hour >= 18
        
        if is_night:
            optimal_density = 0.3
            risk = abs(crowd_density - optimal_density) * 2
        else:
            risk = 1 - crowd_density
        
        return min(max(risk, 0), 1.0)
    
    @staticmethod
    def weather_risk_score(weather: str) -> float:
        weather_risk = {'clear': 0.1, 'rain': 0.4, 'fog': 0.7, 'storm': 0.9}
        return weather_risk.get(weather.lower(), 0.3)
    
    @staticmethod
    def create_features(row: dict) -> dict:
        hour = row.get('hour_of_day', 12)
        
        return {
            'lighting_risk': EnvironmentalFeatureEngineer.lighting_risk_score(
                row.get('street_lighting_score', 0.5), hour
            ),
            'crowd_risk': EnvironmentalFeatureEngineer.crowd_risk_score(
                row.get('crowd_density', 0.5), hour
            ),
            'weather_risk': EnvironmentalFeatureEngineer.weather_risk_score(
                row.get('weather', 'clear')
            ),
        }
