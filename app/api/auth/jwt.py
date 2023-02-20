from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps.user_deps import get_current_user
from app.core.security import create_access_token, create_refresh_token
from app.models.user_model import User
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserOut
from app.services.user_service import UserService

auth_router = APIRouter()

@auth_router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm=Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        return JSONResponse({
                "status": False,
                "message": "Incorrect email or password"
            }, status_code=status.HTTP_400_BAD_REQUEST)
    
    # create access and refresh token
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }


@auth_router.post('/test-token', summary="Test if the access token is valid", response_model=UserOut)
async def test_token(user: User=Depends(get_current_user)):
    return user
