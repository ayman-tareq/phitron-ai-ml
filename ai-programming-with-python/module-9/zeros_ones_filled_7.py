"""zeros (3,3), ones (2,5), full (3,3) of 7, and eye (3)."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    try:
        z = np.zeros((3, 3))
        o = np.ones((2, 5))
        f = np.full((3, 3), 7)
        e = np.eye(3)
        print("zeros (3,3):\n", z, sep="")
        print("ones (2,5):\n", o, sep="")
        print("filled with 7 (3,3):\n", f, sep="")
        print("eye (3):\n", e, sep="")
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
