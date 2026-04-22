"""Lap times (seconds) as NumPy array: shape, size, dtype, times in minutes."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    lap_times_sec = [90.0, 88.5, 91.2, 89.0, 90.5]
    try:
        t = np.array(lap_times_sec)
        print("shape:", t.shape)
        print("size:", t.size)
        print("dtype:", t.dtype)
        minutes = t / 60.0
        print(minutes)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
