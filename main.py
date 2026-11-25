# SPDX-License-Identifier: MIT
"""Write the winning patch note to /output/entry.txt."""
import os

TEXT = "v2.9.6: fixed voice cracking mid-sentence at 34; puberty was never fully uninstalled."


def main() -> None:
    # Deterministic: always writes exactly TEXT, no trailing newline.
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)


if __name__ == "__main__":
    main()
