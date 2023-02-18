from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from beanie import Document, Indexed
from pydantic import EmailStr, Field


class User(Document):
    user_id: str = Field(default_factory=lambda: uuid4().hex)
    username: str = Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]

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