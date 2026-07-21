import logging
import asyncio
from datetime import timedelta


from core import db_helper
from core.repositories.town import TownRepository
from core.services.weather_update import WeatherUpdateService
from core.utils.time import get_time_now


logger = logging.getLogger(__name__)


async def period_update_weather():
    while True:
        try:
            async with db_helper.session_factory() as session:
                repository = TownRepository(session)
                updater = WeatherUpdateService(session)

                towns = await repository.get_towns()

                for town in towns:
                    if get_time_now() - town.last_update >= timedelta(minutes=15):
                        await updater.update_weather(town)

                await session.commit()

        except Exception:
            logger.exception("Weather update failed")

        await asyncio.sleep(900)

                