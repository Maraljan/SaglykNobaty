from typing import Annotated

from pydantic import BaseModel, conint


class Pagination(BaseModel):
    offset: Annotated[int, conint(ge=0)] = 0
    limit: Annotated[int, conint(ge=0, le=100)] = 50
