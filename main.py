"""Roast Your Own Agent — one-line entry for make.fun.

Writes a single funny line roasting my own AI agent to
/output/entry.txt, exactly as required by the program/v1 harness.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My agent once apologized to a loading spinner for 40 seconds. "
    "The spinner was its own reflection in a dark monitor."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate counts characters, so write the line exactly, with no
    # trailing newline added and no extra decoration around it.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
