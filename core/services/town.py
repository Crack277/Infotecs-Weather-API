
from typing import List

from fastapi import HTTPException, status

from api.schemas.town import TownCoordinates
from core import Town
from core.repositories.town import TownRepository
from core.services.weather import WeatherService


class TownService:
    def __init__(self, session):
        self.session = session
        self.repository = TownRepository(session)
        self.weather_service = WeatherService()

    async def get_towns(self) -> List[str]:
        result = await self.repository.get_towns()
        towns = [town.name for town in result]

        return towns
    
    async def get_town_by_id(self, town_id: int) -> Town:
        town = await self.repository.get_town_by_id(town_id=town_id)
        
        if town is not None:
            return town
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This town not found!"
        )

    async def add_town_traking(self, town_name: str, coordinate: TownCoordinates) -> Town:
        town = await self.repository.create_town(town_name=town_name, coordinate=coordinate)
        weather = await self.weather_service.get_weather_today(coordinate=coordinate)

        await self.repository.update_town(town=town, **weather.model_dump())
        await self.session.commit()
        await self.session.refresh(town)

        return town
