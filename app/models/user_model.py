from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import EmailStr, Field


class User(Document):
    # _id: UUID = uuid4().hex
    user_id: str = uuid4().hex
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = False

    def __repr__(self) -> str:
        return f"User {self.email}"
    
    def __str__(self) -> str:
        return self.email
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False
    
    @property
    def create(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(self, email: str) -> "User":
        return await self.find_one(self.email == email)
    
    class Settings:
        name = "users"