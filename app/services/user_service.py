from typing import Optional
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from app.core.security import get_password, verify_password
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
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        
        return user
        
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email==email)
        return user
    
    @staticmethod
    async def get_user_by_id(id: str) -> Optional[User]:
        user = await User.find_one(User.user_id==id)
        return user
