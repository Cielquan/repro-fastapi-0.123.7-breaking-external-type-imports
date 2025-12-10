from __future__ import annotations

import typing as t

import fastapi

from config import get_settings

if t.TYPE_CHECKING:
    import config

app = fastapi.FastAPI()

@app.get("/")
async def dummy(
    settings: config.Settings = fastapi.Depends(get_settings),
) -> str:
    return "Dummy"
