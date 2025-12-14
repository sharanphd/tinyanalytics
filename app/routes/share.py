"""Public share links.

Per ARCHITECTURE.md: read-only public view is optional and unauthenticated.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes.deps import DbDep
from app.services.analytics import create_share_link, get_dashboard, get_share_link

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.post("/share")
def create_share(db: DbDep) -> dict[str, str]:
    link = create_share_link(db=db)
    return {"id": link.id, "url": f"/share/{link.id}"}


@router.get("/share/{share_id}", response_class=HTMLResponse)
def view_share(share_id: str, request: Request, db: DbDep) -> HTMLResponse:
    link = get_share_link(db=db, share_id=share_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Share link not found")

    data = get_dashboard(db=db)
    return templates.TemplateResponse(
        request=request,
        name="share.html",
        context={
            **data,
            "share_id": share_id,
        },
    )
