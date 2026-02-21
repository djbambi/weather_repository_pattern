import json

import polars as pl

from weather_repository_pattern.models import WeatherRecord
from weather_repository_pattern.repository import WeatherRepository


class PolarsWeatherRepository(WeatherRepository):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_weather(self) -> list[WeatherRecord]:
        with open(self.filepath) as f:
            raw = json.load(f)

        # Extract descriptions before creating the DataFrame
        for entry in raw["data"]:
            entry["description"] = entry["weather"][0]["description"]

        df = pl.DataFrame(raw["data"])

        records = []
        for row in df.iter_rows(named=True):
            records.append(
                WeatherRecord(
                    dt=row["dt"],
                    temp=row["temp"],
                    humidity=row["humidity"],
                    description=row["description"],
                )
            )
        return records
