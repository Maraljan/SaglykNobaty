from fastapi import FastAPI


import contextlib
from .core.database import DATA_BASE
from . import auth, appointment_app


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    await DATA_BASE.connect()
    yield None


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(appointment_app.router)
    app.include_router(auth.router)
    return app
