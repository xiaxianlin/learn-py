from pydantic_settings import BaseSettings
from functools import lru_cache


class Setting(BaseSettings):
    database: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Setting()
