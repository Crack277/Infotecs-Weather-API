
from typing import List

from core import User
from api.schemas.user import UserCreate
from repositories.user import UserRepository


class UserService:
    def __init__(self, session):
        self.session = session
        self.repository = UserRepository(session)

    async def get_users(self) -> List[User]:
        return await self.repository.get_users()

    async def create_user(self, user_in: UserCreate) -> User:
        return await self.repository.create_user(user_in=user_in)