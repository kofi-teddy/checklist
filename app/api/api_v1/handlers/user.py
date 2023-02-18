from fastapi import APIRouter

from app.schemas.user_schema import UserAuth

user_router = APIRouter()

@user_router.post('/create', summary="create new user")
async def create_user(data: UserAuth):
    # return {
    #     "message": "user router working"
    # }
    pass
