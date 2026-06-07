"""Pydantic schemas for data validation."""
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class CrimeType(str, Enum):
    ROBBERY = "robbery"
    ASSAULT = "assault"
    THEFT = "theft"
    BURGLARY = "burglary"
    MURDER = "murder"
    CARJACKING = "carjacking"
    SEXUAL_ASSAULT = "sexual_assault"
    OTHER = "other"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ReportType(str, Enum):
    DANGEROUS_AREA = "dangerous_area"
    SUSPICIOUS_ACTIVITY = "suspicious_activity"
    LIGHTING_ISSUE = "lighting_issue"
    UNSAFE_CONDITION = "unsafe_condition"
    SAFE_AREA = "safe_area"


class WeatherCondition(str, Enum):
    CLEAR = "clear"
    RAIN = "rain"
    FOG = "fog"
    STORM = "storm"


class CrimeRecord(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    crime_type: CrimeType
    severity: Severity
    timestamp: datetime
    area_name: Optional[str] = None


class RiskPredictionInput(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    timestamp: datetime
    crowd_density: Optional[float] = 0.5
    lighting_score: Optional[float] = 0.5


class RiskPredictionOutput(BaseModel):
    risk_score: float = Field(ge=0, le=4)
    confidence: float = Field(ge=0, le=1)
    risk_level: str
    risk_class: int = Field(ge=0, le=4)
    
    class Config:
        json_schema_extra = {
            "example": {
                "risk_score": 2.3,
                "confidence": 0.87,
                "risk_level": "Medium Risk",
                "risk_class": 2
            }
        }
