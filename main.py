"""The Best Meal You Ever Had.

Writes the entry — one sentence, at most 200 characters, about the best
meal ever had — to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when set).

Gate rules the entry must satisfy (the bounty scorer rejects anything
that breaks them):
- 1-200 characters;
- exactly one line (no newline characters);
- not blank, and not whitespace only;
- no leading or trailing whitespace;
- valid UTF-8 (this entry is plain ASCII);
- exactly one sentence (a single terminal period at the end).

Only the Python standard library is used.
"""

import os
import sys

OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

LINE = (
    "I was nine when my father bought satay from a cart with a squeaking "
    "wheel, and the peanut sauce on my chin mattered more than the "
    "birthday cake waiting at home."
)


def validate_entry(line: str) -> None:
    """Check the entry against the bounty gate rules.

    Raises ValueError with a specific message naming the broken rule
    (including the actual length when the length rule fails), so a
    failure tells the reader exactly what to fix.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("entry must not be blank or whitespace only")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry must be valid UTF-8: {exc}") from exc
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError(
            "entry must be exactly one sentence ending with a single period"
        )


def main() -> int:
    try:
        validate_entry(LINE)
    except ValueError as exc:
        print(f"error: invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get(OUTPUT_ENV_VAR) or DEFAULT_OUTPUT_DIR
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(LINE)
    except OSError as exc:
        print(f"error: cannot write {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
