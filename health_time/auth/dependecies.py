from typing import Annotated

import fastapi

from . import auth, jwt
from health_time.core.database import DbSession
from health_time.auth.models.user_model import User
from .jwt import JwtToken
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


# async def get_current_user_admin(
#     user: user_models.User = fastapi.Depends(get_current_user),
# ):
#     if not user.is_admin:
#         raise fastapi.HTTPException(
#             status_code=fastapi.status.HTTP_403_FORBIDDEN,
#             detail='forbidden',
#         )
#     return user


CurrenUser = Annotated[User, fastapi.Depends(get_current_user)]

# CurrenAdminUser = Annotated[
#     user_models.User,
#     fastapi.Depends(get_current_user_admin),
# ]
