import asyncio

import uvicorn
from fastapi import FastAPI

from app.infrastructure.config import load_settings


def app_factory() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
    )
    return app


async def run_application() -> None:
    app = app_factory()
    settings = load_settings()
    config = uvicorn.Config(
        app=app,
        host=settings.api.host,
        port=settings.api.port,
        reload=True,
    )
    server = uvicorn.Server(config=config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_application())
