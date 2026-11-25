"""The Best Meal You Ever Had.

Writes the entry — one sentence, at most 200 characters, about the best
meal ever had — to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when set).

Only the Python standard library is used.
"""

import os

LINE = (
    "I was nine when my father bought satay from a cart with a squeaking "
    "wheel, and the peanut sauce on my chin mattered more than the "
    "birthday cake waiting at home."
)


def main() -> None:
    # Guards: the entry must be exactly one sentence of 1-200 characters.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    LINE.encode("ascii")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
