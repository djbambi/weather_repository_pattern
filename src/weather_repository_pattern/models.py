from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherRecord:
    dt: int  # Unix timestamp
    temp: float  # Temperature in Celsius
    humidity: int  # Humidity percentage
    description: str  # Weather description (e.g., "overcast clouds")
