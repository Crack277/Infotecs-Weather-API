
from typing import List

from fastapi import HTTPException, status

from core import User
from api.schemas.user import UserCreate
from core.repositories.user import UserRepository


class UserService:
    def __init__(self, session):
        self.session = session
        self.repository = UserRepository(session)

    async def get_users(self) -> List[User]:
        return await self.repository.get_users()

    async def create_user(self, user_in: UserCreate) -> User:
        user = await self.repository.create_user(user_in=user_in)
        if user is not None:
            await self.session.commit()
            await self.session.refresh(user)
            return user
        
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This user already register!"
        )
        