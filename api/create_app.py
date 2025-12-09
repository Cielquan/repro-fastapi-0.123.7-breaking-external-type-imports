from __future__ import annotations

import fastapi

from .routers import dummy


def create_app() -> fastapi.FastAPI:
    """Create API app."""
    return fastapi.FastAPI()
