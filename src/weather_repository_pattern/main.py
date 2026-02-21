from weather_repository_pattern.pandas_repository import PandasWeatherRepository
from weather_repository_pattern.polars_repository import PolarsWeatherRepository
from weather_repository_pattern.weather_summary import weather_summary

if __name__ == "__main__":
    # Using pandas
    pandas_repo = PandasWeatherRepository("weather_data.json")
    print("=== Pandas Repository ===")
    weather_summary(pandas_repo)

    # Using polars
    polars_repo = PolarsWeatherRepository("weather_data.json")
    print("\n=== Polars Repository ===")
    weather_summary(polars_repo)
