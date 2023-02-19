from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from app.core.security import get_password
from app.core.utils import CustomHTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserAuth


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        if await User.find_one({"username": user.username}):
            return JSONResponse({
                "status": False,
                "message": "User with this username already exists"
            }, status_code=status.HTTP_400_BAD_REQUEST)
        
        if await User.find_one({"email": user.email}):
            return JSONResponse({
                "status": False,
                "message": "User with this email already exists"
            }, status_code=status.HTTP_400_BAD_REQUEST)

        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in
