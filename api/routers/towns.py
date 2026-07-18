from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from services.town import TownService


router = APIRouter(prefix="/towns", tags=["TOWNS"])


@router.get("/")
async def get_towns(
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    service = TownService(session=session)
    return await service.get_towns()


@router.get("/{town_id}/")
async def get_town_by_id(
    town_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    service = TownService(session=session)
    return await service.get_town_by_id(town_id=town_id)