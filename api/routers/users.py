from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.user import UserCreate
from core import db_helper
from services.user import UserService

router = APIRouter(prefix="/users", tags=["USERS"])

@router.get("/all")
async def get_users(
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    service = UserService(session=session)
    return await service.get_users()

@router.post("/")
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    service = UserService(session=session)
    return await service.create_user(user_in=user_in)