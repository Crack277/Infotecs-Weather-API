
from sqlalchemy.ext.asyncio import AsyncSession

from core import Town
from api.schemas.town import TownCoordinates
from core.repositories.town import TownRepository
from core.services.weather import WeatherService
from core.utils.time import get_time_now


class WeatherUpdateService:
    def __init__(self, session: AsyncSession):
        self.town_repository = TownRepository(session)
        self.weather_service = WeatherService()

    async def update_weather(self, town: Town):
        weather = await self.weather_service.get_weather_today(
            coordinate=TownCoordinates(
                latitude=town.latitude,
                longitude=town.longitude
            )
        )

        await self.town_repository.update_town(
            town,
            **weather.model_dump(),
            last_update = get_time_now()
        )
        