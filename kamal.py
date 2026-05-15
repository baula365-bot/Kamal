#!/usr/bin/env python3
"""Command-line entry point for the Kamal Telegram tools project."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class AppInfo:
    """Basic application metadata displayed by the CLI."""

    name: str = "Kamal"
    description: str = "Telegram tools"
    python_version: str = "3.11"


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for the Kamal entry point."""
    app_info = AppInfo()
    parser = argparse.ArgumentParser(
        prog="kamal.py",
        description=f"{app_info.name}: {app_info.description}",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{app_info.name} CLI for Python {app_info.python_version}",
    )
    return parser


def main() -> int:
    """Run the Kamal command-line entry point."""
    parser = build_parser()
    parser.parse_args()

    app_info = AppInfo()
    print(f"{app_info.name} - {app_info.description}")
    print("Ready to add Telegram tooling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
