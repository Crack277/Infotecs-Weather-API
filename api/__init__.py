from fastapi import APIRouter

from .routers.towns import router as town_router
from .routers.users import router as user_router


router = APIRouter()
router.include_router(user_router)
router.include_router(town_router)