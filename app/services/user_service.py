from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from app.core.security import get_password
from app.core.utils import CustomHTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserAuth


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user = await User.find_one({"username": user.username}) or  User.find_one({"email": user.email})
        if user:
            # raise HTTPException(
            #     status_code=status.HTTP_400_BAD_REQUEST, 
            #     detail="User with this username or email already exists")
            # raise CustomHTTPException(status_code=400, detail="Bad Request", additional_data={"field": "value"})
            # raise CustomHTTPException(status_code=404, detail="User not found", additional_data={"user_id": "1234"})
            # raise CustomHTTPException(status_code=400, detail="User already exists", additional_data={"user_id": "1234"})
            return JSONResponse({
                "status": False,
                "message": "User with this username or email already exists"
            }, status_code=status.HTTP_400_BAD_REQUEST)

        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in
