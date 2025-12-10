from __future__ import annotations

import typing as t

import fastapi

if t.TYPE_CHECKING:
    import config


router = fastapi.APIRouter(tags=["Dummy"], prefix="/dummy")


@router.get("/")
async def dummy(
    settings: config.Settings,
) -> str:
    """Check API status."""
    return "Dummy"
