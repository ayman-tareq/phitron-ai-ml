"""Load `.env` from the repository root (two levels above this package)."""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv


def load_project_env() -> None:
    root = Path(__file__).resolve().parents[2]
    load_dotenv(root / ".env")
