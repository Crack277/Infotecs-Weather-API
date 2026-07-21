import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import router as api_router
from core import Base, db_helper
from core.tasks.weather import period_update_weather


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    task = asyncio.create_task(period_update_weather())

    yield

    task.cancel()
    

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("script:app", reload=True)


