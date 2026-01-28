from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("")
def health() -> dict:
    return {"status": "ok", "env": settings.ENV}
