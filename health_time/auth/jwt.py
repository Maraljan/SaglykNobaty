import datetime
import json
from enum import StrEnum
from typing import Self

from fastapi.exceptions import HTTPException
from fastapi import status

from pydantic import BaseModel, EmailStr, ValidationError, Field

import jose
import jose.jwt
from health_time import config


class TokenType(StrEnum):
    BEARER = 'bearer'


class TokenResponse(BaseModel):
    access_token: str
    token_type: TokenType = TokenType.BEARER


class JwtToken(BaseModel):
    email: EmailStr
    expire: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.utcnow()+datetime.timedelta(days=config.jwt_access_expire_days))

    @classmethod
    def decode(cls, token: str) -> Self:
        try:
            payload = jose.jwt.decode(
                token=token,
                key=config.jwt_access_token_secret,
                algorithms=[config.jwt_algorithm]
            )
            token = cls.parse_obj(payload)
        except (jose.JWTError, ValidationError):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

        token.check_expire()
        return token

    def encode(self) -> str:
        return jose.jwt.encode(
            claims=json.loads(self.json()),
            key=config.jwt_access_token_secret,
            algorithm=config.jwt_algorithm,
        )

    def check_expire(self):
        if self.expire < datetime.datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has been expired!')
