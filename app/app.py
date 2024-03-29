from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.api_v1.router import router
from app.core.config import settings
from app.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.get('/')
async def hello():
    return {
        "message": "Hello hero!"
    }


@app.on_event("startup")
async def app_init():
    """
    initialize crutial application services
    """
    # db_client = AsyncIOMotorClient(settings.MANGO_CONNECTION_STRING)
    client = AsyncIOMotorClient(settings.MANGO_CONNECTION_STRING)
    db_client = client["Cluster0"]

    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

app.include_router(router, prefix=settings.API_V1_STR)