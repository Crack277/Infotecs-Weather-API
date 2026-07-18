
from typing import List

from fastapi import HTTPException, status

from core.models.town import Town
from repositories.town import TownRepository


class TownService:
    def __init__(self, session):
        self.session = session
        self.repository = TownRepository(session)

    async def get_towns(self) -> List[Town]:
        return await self.repository.get_towns()
    
    async def get_town_by_id(self, town_id: int) -> Town:
        town = await self.repository.get_town_by_id(town_id=town_id)\
        
        if town is not None:
            return town
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This town not found!"
        )
    