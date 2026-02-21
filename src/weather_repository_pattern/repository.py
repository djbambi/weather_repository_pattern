from abc import ABC, abstractmethod

from models import WeatherRecord


class WeatherRepository(ABC):
    @abstractmethod
    def get_weather(self) -> list[WeatherRecord]:
        """Return a list of WeatherRecords from some data source."""
        ...
