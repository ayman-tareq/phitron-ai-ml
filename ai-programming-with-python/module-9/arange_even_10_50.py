"""Even numbers from 10 to 50 (inclusive) with arange."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    try:
        a = np.arange(10, 51, 2)
        print(a)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
