"""1D, 2D, and 3D NumPy arrays: print dimensions and shapes."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import numpy as np
    except ImportError:
        print("numpy is required: pip install numpy", file=sys.stderr)
        return 1

    try:
        one_d = np.array([1, 2, 3, 4, 5])
        two_d = np.array([[1, 2, 3], [4, 5, 6]])
        three_d = np.arange(24).reshape(2, 3, 4)

        for name, arr in (("1D", one_d), ("2D", two_d), ("3D", three_d)):
            print(f"{name} array:\n{arr!r}")
            print(f"  ndim (dimensions): {arr.ndim}")
            print(f"  shape: {arr.shape}\n")
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
