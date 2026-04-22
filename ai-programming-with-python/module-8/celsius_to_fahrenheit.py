"""Celsius list → NumPy array → Fahrenheit (F = C * 1.8 + 32)."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    celsius = [0, 15, 25, 37, 100]
    try:
        c = np.array(celsius, dtype=np.float64)
        f = c * 1.8 + 32
        print(f)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
