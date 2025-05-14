from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import router
from core import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app():
    app = FastAPI(
        debug=settings.debug,
        title="Base Template",
        lifespan=lifespan,
    )
    app.include_router(router)
    return app


if __name__ == "__main__":
    uvicorn.run(
        app="main:create_app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=True,
        factory=True,
    )
