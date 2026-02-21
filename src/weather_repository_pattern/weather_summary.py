from weather_repository_pattern.repository import WeatherRepository


def weather_summary(repo: WeatherRepository) -> None:
    records = repo.get_weather()

    avg_temp = sum(r.temp for r in records) / len(records)
    avg_humidity = sum(r.humidity for r in records) / len(records)

    print(f"Total records: {len(records)}")
    print(f"Average temperature: {avg_temp:.1f}°C")
    print(f"Average humidity: {avg_humidity:.1f}%")
    for r in records:
        print(f"  {r.dt} | {r.temp}°C | {r.humidity}% | {r.description}")
