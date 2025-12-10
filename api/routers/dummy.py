from __future__ import annotations

import typing as t

import fastapi

from api.dependencies.config import get_settings

if t.TYPE_CHECKING:
    import config


router = fastapi.APIRouter(tags=["Dummy"], prefix="/dummy")


@router.get("/")
async def dummy(
    settings: config.Settings = fastapi.Depends(get_settings),
) -> str:
    """Check API status."""
    return "Dummy"
