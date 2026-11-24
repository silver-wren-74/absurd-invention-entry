#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — writes one sentence to /output/entry.txt."""
import os

LINE = "Introducing the Sock Reunion Service: a washing machine that, the moment it swallows one sock, prints a missing poster for it and goes on laundry strike until the pair is reunited."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
