
from typing import List

from sqlalchemy import select

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
    
    async def create_town(self):
        pass
    