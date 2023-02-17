from typing import List

from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRATION_MINUTES: int = 60 * 24 * 7 #days
    PROJECT_NAME: str = "Checklist"
    MANGO_CONNECTION_STRING: str = config("MANGO_CONNECTION_STRING", cast=str)


class Config:
    case_sensitive = True


settings = Settings()



