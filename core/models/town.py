from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Town(Base):
    name: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    temperature: Mapped[List[float]] = mapped_column(JSON)
    relative_humidity: Mapped[List[float]] = mapped_column(JSON)
    wind_speed: Mapped[List[float]] = mapped_column(JSON)
    precipitation: Mapped[List[float]] = mapped_column(JSON)
    last_update: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(back_populates="town")