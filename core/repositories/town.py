
from typing import List
from sqlalchemy import select

from api.schemas.town import TownCoordinates
from core.utils.time import get_time_now
from core import Town


class TownRepository:
    def __init__(self, session):
        self.session = session

    async def get_towns(self) -> List[Town]:
        stmt = select(Town).order_by(Town.id)
        result = await self.session.execute(stmt)
        towns = result.scalars().all()
        return list(towns)
    
    async def get_town_by_id(self, town_id: int) -> Town | None:
        return await self.session.get(Town, town_id)
    
    async def get_town_by_name(self, town_name: str) -> Town | None:
        stmt = select(Town).where(Town.name == town_name)
        town = await self.session.scalar(stmt)
        return town
    
    async def create_town(self, town_name: str, coordinate: TownCoordinates) -> Town:
        town = Town(
            **coordinate.model_dump(),
            name=town_name,
            last_update=get_time_now()
        )
        self.session.add(town)
        return town
    
    async def update_town(self, town: Town, **values) -> Town:
        for key, value in values.items():
            setattr(town, key, value)

        return town