from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/", tags=["root"])
def root() -> dict:
    return {"name": settings.APP_NAME, "env": settings.ENV}
