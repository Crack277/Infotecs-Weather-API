import httpx

from api.schemas.town import CoordinatesResponse, TownCoordinates, TownWeather
from core.config import settings
from core.utils.time import nearest_time, get_time_now


class WeatherService:
    async def get_weather(self, coordinate: TownCoordinates):
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                settings.api_url,
                params={
                    "latitude": coordinate.latitude,
                    "longitude": coordinate.longitude,
                    "current": "temperature_2m,wind_speed_10m",
                    "hourly": (
                        "temperature_2m,"
                        "precipitation,"
                        "relative_humidity_2m,"
                        "wind_speed_10m,"
                        "pressure_msl"
                ),
                }
            )
            response.raise_for_status()
            return response.json()

    async def get_weather_now(self, coordinate: TownCoordinates):
        weather = await self.get_weather(coordinate=coordinate)
 
        time = nearest_time(get_time_now())
        time_index = weather["hourly"]["time"].index(time)

        response = CoordinatesResponse(
            time=time,
            temperature=weather["hourly"]["temperature_2m"][time_index],
            wind_speed=weather["hourly"]["wind_speed_10m"][time_index],
            pressure=weather["hourly"]["pressure_msl"][time_index]
        )
        return response
    
    async def get_weather_today(self, coordinate: TownCoordinates):
        weather = await self.get_weather(coordinate=coordinate)
        date = nearest_time(get_time_now()).split("T")[0] # Берём сегодняшний день

        result = TownWeather(
            temperature=[],
            relative_humidity=[],
            wind_speed=[],
            precipitation=[],
        )

        hourly = weather["hourly"]

        for i, timestamp in enumerate(hourly["time"]):
            if timestamp.startswith(date):
                result.temperature.append(hourly["temperature_2m"][i])
                result.relative_humidity.append(hourly["relative_humidity_2m"][i])
                result.wind_speed.append(hourly["wind_speed_10m"][i])
                result.precipitation.append(hourly["precipitation"][i])

        return result

