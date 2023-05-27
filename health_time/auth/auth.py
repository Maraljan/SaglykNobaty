import passlib.context

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from health_time import config

from health_time.core.database import DbSession

from health_time.core.storage import user_storage

from .models.user_model import User


class Auth:
    def __init__(self):
        self._crypto_ctx = passlib.context.CryptContext(
            schemes=[config.password_algorithm],
            deprecated='auto',
        )
        self.oauth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

    def hash_password(
            self,
            password: str,
    ) -> str:
        return self._crypto_ctx.hash(password)

    def verify_password(
            self,
            plain_password: str,
            hashed_password: str,
    ) -> bool:
        return self._crypto_ctx.verify(
            secret=plain_password,
            hash=hashed_password,
        )

    async def auth_user(
            self,
            session: DbSession,
            email: str,
            password: str,
    ) -> User:
        storage = user_storage.UserStorage(session)
        user = await storage.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Authorized user could not be found',
            )

        if not self.verify_password(
                plain_password=password,
                hashed_password=user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Wrong password',
            )

        return user


AUTH = Auth()



