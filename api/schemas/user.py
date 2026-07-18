

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str


class UserCreate(UserSchema):
    pass