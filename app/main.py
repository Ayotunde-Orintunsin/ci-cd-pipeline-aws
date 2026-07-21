from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import configure_logging
from app.db.base import Base
from app.db.session import engine
from app.routers import health, tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="ci-cd-pipeline-aws", lifespan=lifespan)
app.include_router(health.router)
app.include_router(tasks.router)
