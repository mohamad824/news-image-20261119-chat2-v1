#!/usr/bin/env python3
"""chat2-v1 entrypoint: copy the shipped image to the output directory.

Stdlib only. Deterministic: copies bytes unchanged, so repeated runs
are byte-identical. Never deletes the output directory.
"""
import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("image.png missing next to main.py\n")
        return 1
    # Byte-for-byte copy: deterministic, no re-encoding, no timestamp
    # dependence, so two runs write identical bytes.
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        shutil.copyfileobj(fin, fout, length=1024 * 1024)
    return 0


if __name__ == "__main__":
    sys.exit(main())
