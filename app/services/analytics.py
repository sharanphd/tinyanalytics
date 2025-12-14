"""Analytics domain logic.

Keeps route handlers thin and testable.
"""

from __future__ import annotations

import datetime as dt
import hashlib
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import HASH_SALT
from app.db.models import Page, PageView, ShareLink


def hash_ip(ip: str) -> str:
    # Immediate hashing per ARCHITECTURE.md. Salt is optional but recommended.
    raw = (HASH_SALT + ip).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def record_page_view(*, db: Session, url: str, client_ip: str) -> None:
    now = dt.datetime.utcnow()
    pv = PageView(url=url, timestamp=now, hashed_ip=hash_ip(client_ip))
    db.add(pv)

    page = db.get(Page, url)
    if page is None:
        page = Page(url=url, total_views=0)
        db.add(page)

    page.total_views += 1
    db.commit()


def get_dashboard(*, db: Session, limit: int = 50) -> dict[str, Any]:
    total_pageviews = db.scalar(select(func.count()).select_from(PageView)) or 0

    pages = db.execute(
        select(Page.url, Page.total_views).order_by(Page.total_views.desc(), Page.url.asc()).limit(limit)
    ).all()

    return {
        "total_pageviews": total_pageviews,
        "pages": [{"url": url, "total_views": total_views} for (url, total_views) in pages],
    }


def create_share_link(*, db: Session) -> ShareLink:
    link = ShareLink()
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


def get_share_link(*, db: Session, share_id: str) -> ShareLink | None:
    return db.get(ShareLink, share_id)
