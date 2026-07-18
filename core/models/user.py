from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .town import Town


class User(Base):
    name: Mapped[str]

    town: Mapped[list["Town"]] = relationship(back_populates="user")