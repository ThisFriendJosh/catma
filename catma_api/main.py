"""Minimal FastAPI application."""

try:  # pragma: no cover - optional dependency
    from fastapi import FastAPI
except Exception:  # pragma: no cover
    FastAPI = None
    app = None
else:  # pragma: no cover
    app = FastAPI()

    @app.get("/")
    def read_root():  # pragma: no cover
        return {"message": "Catma API"}
