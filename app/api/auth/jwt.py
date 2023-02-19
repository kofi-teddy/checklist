from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService

auth_router = APIRouter()

@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm):
    user = await UserService.authenticate(email=form_data.email, password=form_data.password)