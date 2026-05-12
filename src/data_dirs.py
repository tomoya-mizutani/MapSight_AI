#!/usr/bin/env python3
"""Utility for creating standard data directory structure.

This script helps managing match data by automatically creating
folders for scrims and tournaments.

Usage:
    python data_dirs.py scrim YYYY/MM/DD [--rounds N]
    python data_dirs.py tournament NAME
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def create_scrim(date_str: str, rounds: int = 2, root: Path | str = "data") -> Path:
    """Create ``data/Scrim/YYYY/MM/DD/RoundX`` directories.

    Parameters
    ----------
    date_str : str
        Date string in ``YYYY/MM/DD`` format.
    rounds : int, optional
        Number of round subdirectories to create, by default ``2``.
    root : Path | str, optional
        Root data directory, by default ``"data"``.

    Returns
    -------
    Path
        Path to the created date directory.
    """
    root_path = Path(root)
    try:
        dt = datetime.strptime(date_str, "%Y/%m/%d")
    except ValueError as e:
        raise ValueError("date must be in YYYY/MM/DD format") from e

    base = root_path / "Scrim" / dt.strftime("%Y") / dt.strftime("%m") / dt.strftime("%d")
    base.mkdir(parents=True, exist_ok=True)
    for i in range(1, rounds + 1):
        (base / f"Round{i}").mkdir(exist_ok=True)
    return base


def create_tournament(name: str, root: Path | str = "data") -> Path:
    """Create ``data/tournament/<name>`` directory."""
    path = Path(root) / "tournament" / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create data directories")
    sub = parser.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scrim", help="create scrim date/round directories")
    s.add_argument("date", help="date in YYYY/MM/DD format")
    s.add_argument("--rounds", type=int, default=2, help="number of rounds")

    t = sub.add_parser("tournament", help="create tournament directory")
    t.add_argument("name", help="tournament name")

    args = parser.parse_args()
    if args.cmd == "scrim":
        out = create_scrim(args.date, args.rounds)
    else:
        out = create_tournament(args.name)
    print(out)


if __name__ == "__main__":
    main()
