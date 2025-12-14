"""Tracking endpoint.

No cookies, no auth, no third-party telemetry.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, HttpUrl

from app.routes.deps import DbDep
from app.services.analytics import record_page_view

router = APIRouter()


class TrackPayload(BaseModel):
    url: HttpUrl


@router.post("/track", status_code=204)
def track(payload: TrackPayload, request: Request, db: DbDep) -> Response:
    client = request.client
    if client is None or not client.host:
        raise HTTPException(status_code=400, detail="Client IP missing")

    record_page_view(db=db, url=str(payload.url), client_ip=client.host)
    return Response(status_code=204)
