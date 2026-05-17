"""Maavnica Profile — profils vivants multi-personas (JSON local, SSR léger)."""

import json
import re
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

APP_DIR = Path(__file__).resolve().parent
BACKEND_DIR = APP_DIR.parent
PROFILE_DIR = (BACKEND_DIR / "static" / "profile").resolve()
DATA_DIR = (PROFILE_DIR / "data").resolve()
TEMPLATES = Jinja2Templates(directory=str(APP_DIR / "templates"))

SLUG_RE = re.compile(r"^[a-z0-9-]+$")


def known_slugs() -> tuple[str, ...]:
    return tuple(sorted(p.stem for p in DATA_DIR.glob("*.json")))


app = FastAPI(
    title="Maavnica Profile",
    description="Profils professionnels publics — JSON local, sans base de données.",
)


def load_profile(slug: str) -> dict[str, Any] | None:
    """Charge data/{slug}.json si le slug est valide et le fichier existe."""
    if not SLUG_RE.match(slug):
        return None
    path = DATA_DIR / f"{slug}.json"
    if not path.is_file():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/p/arnaud", status_code=302)


@app.get("/p/{slug}")
async def public_profile(request: Request, slug: str):
    profile = load_profile(slug)
    if profile is None:
        return TEMPLATES.TemplateResponse(
            request,
            "not_found.html",
            {"slug": slug, "known_slugs": known_slugs()},
            status_code=404,
        )
    return TEMPLATES.TemplateResponse(
        request,
        "profile.html",
        {"profile": profile},
    )


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.mount(
    "/static/profile",
    StaticFiles(directory=str(PROFILE_DIR)),
    name="profile_static",
)
