

from typing import List

from pydantic import BaseModel


class TownCoordinates(BaseModel):
    latitude: float # <= 90
    longitude: float # <= 100


class TownSchema(BaseModel):
    temperature: List[float]
    relative_humidity: List[float]
    wind_speed: List[float]
    precipitation: List[float]