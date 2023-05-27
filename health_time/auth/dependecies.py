from typing import Annotated

import fastapi

from . import auth
from .jwt import JwtToken
from .models.user_model import User
from .models.role_model import RoleName
from health_time.core.database import DbSession
from health_time.core.storage.user_storage import UserStorage


async def auth_user_by_token(
    session: DbSession,
    token: JwtToken,
):
    user_storage = UserStorage(session)
    user = await user_storage.get_by_email(token.email)

    if user is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail='Authorized user could not be found',
        )

    return user


async def get_current_user(
        session: DbSession,
        access_raw_token: str = fastapi.Depends(auth.AUTH.oauth_scheme),
) -> User:
    token = JwtToken.decode(access_raw_token)
    return await auth_user_by_token(session, token)


async def get_current_user_admin(
    user: User = fastapi.Depends(get_current_user),
):
    if user.user_role.role_name != RoleName.ADMIN:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_403_FORBIDDEN,
            detail='forbidden',
        )
    return user


async def get_current_patient(
    user: User = fastapi.Depends(get_current_user),
):
    if user.user_role.role_name != RoleName.PATIENT:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_403_FORBIDDEN,
            detail='forbidden',
        )
    return user


async def get_current_doctor(
    user: User = fastapi.Depends(get_current_user),
):
    if user.user_role.role_name != RoleName.DOCTOR:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_403_FORBIDDEN,
            detail='forbidden',
        )
    return user


CurrentUser = Annotated[User, fastapi.Depends(get_current_user)]

CurrentAdminUser = Annotated[
    User,
    fastapi.Depends(get_current_user_admin),
]

CurrentPatient = Annotated[User, fastapi.Depends(get_current_patient)]
CurrentDoctor = Annotated[User, fastapi.Depends(get_current_doctor)]
