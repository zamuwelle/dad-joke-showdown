"""Deliver the dinner-table joke as plain text."""

from pathlib import Path
from os import getenv


def main() -> None:
    output = Path(getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    joke = "My kid asked why I put the grocery receipt in the blender. I told her I was cutting costs."
    (output / "entry.txt").write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
