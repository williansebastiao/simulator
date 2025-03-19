from fastapi import APIRouter

from . import health, simulation

router = APIRouter()

router.include_router(health.router)
router.include_router(simulation.router)
