from app.schemas.user_schema import UserAuth
from app.models.user_model import User


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=user.password
        )
