from datetime import datetime
from typing import Optional

from fastapi import APIRouter

from src.infra.repo import periodic_tasks_repo

from .crontab_schedules import router as crontab_scheduler_router
from .interval_schedules import router as interval_schedules_router
from .periodic_tasks import router as periodic_task_router

router = APIRouter()

router.include_router(
    interval_schedules_router,
    prefix="/interval_schedules",
    tags=["Interval Schedules"],
)

router.include_router(
    crontab_scheduler_router,
    prefix="/crontab_schedules",
    tags=["Crontab Schedules"],
)

router.include_router(
    periodic_task_router,
    prefix="/periodic_tasks",
    tags=["Periodic Tasks"],
)


@router.get("/last_update", response_model=Optional[datetime])
def last_update() -> Optional[datetime]:
    if (obj := periodic_tasks_repo.get()) is None:
        return None
    else:
        return obj.last_update
