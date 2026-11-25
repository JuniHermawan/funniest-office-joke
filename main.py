#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one line about office life to /output/entry.txt (or $OUTPUT_DIR).
Stdlib only, deterministic, no network.
"""

import os

ENTRY = "I survived a meeting that could've been an email by replying all: 'Per my last email, this meeting.'"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
