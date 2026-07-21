from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

router = APIRouter(tags=["health"])

@router.get("/health")
def health():
    """Liveness: is the process up."""
    return {"status": "ok"}

@router.get("/ready")
async def ready(db: AsyncSession = Depends(get_db)):
    """Readiness: can we actually serve traffic (DB reachable)."""
    await db.execute(text("SELECT 1"))
    return {"status": "ready"}
