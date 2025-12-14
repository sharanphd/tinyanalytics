"""Dashboard UI (server-rendered HTML + HTMX partials)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes.deps import DbDep
from app.services.analytics import get_dashboard

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: DbDep) -> HTMLResponse:
    data = get_dashboard(db=db)
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            **data,
        },
    )


@router.get("/partials/pages", response_class=HTMLResponse)
def pages_partial(request: Request, db: DbDep) -> HTMLResponse:
    data = get_dashboard(db=db)
    return templates.TemplateResponse(
        request=request,
        name="partials/pages.html",
        context={
            **data,
        },
    )
