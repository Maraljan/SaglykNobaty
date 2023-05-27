from fastapi import APIRouter, Depends

from health_time.auth.models.user_model import UserGet
from health_time.core.database import DbSession
from fastapi.security import OAuth2PasswordRequestForm
from health_time.auth.jwt import TokenResponse, JwtToken
from health_time.auth.auth import AUTH
from health_time.auth.dependecies import CurrenUser

router = APIRouter(prefix='/login', tags=['Auth'])


@router.post('/')
async def login(session: DbSession, form: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    user = await AUTH.auth_user(session, email=form.username, password=form.password)
    return TokenResponse(
        access_token=JwtToken(email=user.email).encode()
    )


@router.get('/current_user')
async def get_current_user(user: CurrenUser) -> UserGet:
    return user
