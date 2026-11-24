#!/usr/bin/env python3
"""Entry for make.fun bounty: fortune-cookie wisdom for developers.

Writes one original line of fortune-cookie wisdom aimed at a software
developer to the output directory (``/output/entry.txt`` by default, or
``$MAKEFUN_OUTPUT`` when set).

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os

MAX_LENGTH = 120

ENTRY = (
    "The bug you ignore at 3 p.m. will page you at 3 a.m. \u2014 "
    "fix it now, while it still fears you."
)


def validate(text: str) -> None:
    """The entry must be a single line of 1-120 characters.

    Rejects empty or over-long entries, leading/trailing whitespace,
    embedded newlines, and control characters (a fortune-cookie line
    must be plain printable text on one line).
    """
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} characters, got {len(text)}"
        )
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")


def resolve_out_path() -> str:
    """Resolve the output file path.

    ``$MAKEFUN_OUTPUT`` may point at a directory (``entry.txt`` is written
    inside it) or directly at a file (used as-is); the default is
    ``/output/entry.txt``, falling back to ``./output/entry.txt``.
    """
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output/entry.txt"
    if requested.endswith(".txt"):
        # A direct file path: make sure its parent directory exists first.
        parent = os.path.dirname(requested)
        if parent:
            try:
                os.makedirs(parent, exist_ok=True)
            except OSError:
                return os.path.join(os.getcwd(), "output", "entry.txt")
        return requested
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return os.path.join(requested, "entry.txt")
    except OSError:
        return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> int:
    validate(ENTRY)
    path = resolve_out_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the written file by reading it back: content and length
    # must both match exactly, so a truncated or altered write is caught.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written) != len(ENTRY):
        raise RuntimeError("verification failed: written entry does not match")
    print(f"wrote {len(ENTRY)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
