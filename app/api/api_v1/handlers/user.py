import pymongo
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError

from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService

user_router = APIRouter()

@user_router.post('/create', summary="create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        user = await UserService.create_user(data)
        return user
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            default="User with this email or username already exist"
        )
