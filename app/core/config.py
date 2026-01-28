from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field


def _to_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


def _load_env_files() -> None:
    root = Path(__file__).resolve().parents[2]

    base = root / ".env"
    if base.exists():
        load_dotenv(base, override=False)

    env = os.getenv("ENV", "dev")
    env_file = root / f".env.{env}"
    if env_file.exists():
        load_dotenv(env_file, override=True)


class Settings(BaseModel):
    ENV: str = Field(default="dev")
    APP_NAME: str = Field(default="awaves-backend")
    DEBUG: bool = Field(default=False)
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)
    API_PREFIX: str = Field(default="/api/v1")

    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/awaves"
    )
    DB_ECHO: bool = Field(default=False)
    REDIS_URL: str = Field(default="redis://localhost:6379/0")

    JWT_SECRET: str = Field(default="CHANGE_ME")
    JWT_ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)

    AWS_REGION: str = Field(default="ap-northeast-2")
    LOG_LEVEL: str = Field(default="INFO")


@lru_cache
def get_settings() -> Settings:
    _load_env_files()

    return Settings(
        ENV=os.getenv("ENV", "dev"),
        APP_NAME=os.getenv("APP_NAME", "awaves-backend"),
        DEBUG=_to_bool(os.getenv("DEBUG"), False),
        HOST=os.getenv("HOST", "0.0.0.0"),
        PORT=int(os.getenv("PORT", "8000")),
        API_PREFIX=os.getenv("API_PREFIX", "/api/v1"),
        DATABASE_URL=os.getenv(
            "DATABASE_URL",
            "postgresql+asyncpg://postgres:postgres@localhost:5432/awaves",
        ),
        DB_ECHO=_to_bool(os.getenv("DB_ECHO"), False),
        REDIS_URL=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        JWT_SECRET=os.getenv("JWT_SECRET", "CHANGE_ME"),
        JWT_ALGORITHM=os.getenv("JWT_ALGORITHM", "HS256"),
        ACCESS_TOKEN_EXPIRE_MINUTES=int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
        ),
        AWS_REGION=os.getenv("AWS_REGION", "ap-northeast-2"),
        LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO"),
    )


settings = get_settings()
