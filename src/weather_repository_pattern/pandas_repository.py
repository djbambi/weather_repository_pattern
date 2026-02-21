import json

import pandas as pd
from models import WeatherRecord
from repository import WeatherRepository


class PandasWeatherRepository(WeatherRepository):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_weather(self) -> list[WeatherRecord]:
        with open(self.filepath) as f:
            raw = json.load(f)

        df = pd.DataFrame(raw["data"])

        records = []
        for _, row in df.iterrows():
            records.append(
                WeatherRecord(
                    dt=row["dt"],
                    temp=row["temp"],
                    humidity=row["humidity"],
                    description=row["weather"][0]["description"],
                )
            )
        return records
