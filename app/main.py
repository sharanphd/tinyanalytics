"""FastAPI application entrypoint."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.db.init_db import init_db
from app.routes import dashboard, share, track

from app.routes.health import router as health_router


app = FastAPI(title="TinyAnalytics")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(dashboard.router)
app.include_router(track.router)
app.include_router(share.router)
app.include_router(health_router)


@app.on_event("startup")
def _startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
