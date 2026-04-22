"""4×4 matrix 0–15: first row, last column, center 2×2 subarray."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    try:
        m = np.arange(16).reshape(4, 4)
        first_row = m[0, :]
        last_col = m[:, -1]
        center = m[1:3, 1:3]
        print("matrix:\n", m, sep="")
        print("first row:", first_row)
        print("last column:", last_col)
        print("center 2x2:\n", center, sep="")
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
