from fastapi import FastAPI


import contextlib

from fastapi.middleware import cors

from .core.database import DATA_BASE
from . import auth, appointment_app, patient_cabinet_app


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    await DATA_BASE.connect()
    yield None


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(appointment_app.router)
    app.include_router(auth.router)
    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    app.include_router(patient_cabinet_app.router)
    return app
