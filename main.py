#!/usr/bin/env python3
"""The One-Liner Groan-Off — one original dad joke."""
import os

LINE = "I told my wife she should embrace her mistakes. She hugged me."
assert len(LINE) == 62, "entry must be exactly 62 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
