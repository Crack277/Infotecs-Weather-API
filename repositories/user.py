

from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select

from api.schemas.user import UserCreate
from core import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    async def get_users(self) -> List[User]:
        stmt = select(User).order_by(User.id)
        result = await self.session.execute(stmt)
        users = result.scalars().all()
        return list(users)

    async def create_user(self, user_in: UserCreate):
        stmt = select(User).where(User.name == user_in.name)
        result = await self.session.scalar(stmt)

        if result is None:
            user = User(**user_in.model_dump())
            self.session.add(user)
            await self.session.commit()
            return user

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This user already register!"
        )