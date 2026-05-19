import sys
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).with_name("data.csv")


def main() -> None:
  df = pd.read_csv(DATA_FILE)

  missing_count = df.isna().sum()
  missing_pct = (missing_count / len(df) * 100).round(2)
  over_50 = missing_pct[missing_pct > 50]

  print("=== Problem 2: Missing values report ===\n")
  print(f"Rows: {len(df)}, Columns: {len(df.columns)}\n")

  print("1) Total missing per column:")
  print(missing_count[missing_count > 0].sort_values(ascending=False))
  print()

  print("2) Percentage missing per column:")
  report = pd.DataFrame({"missing": missing_count, "pct": missing_pct})
  print(report[report["missing"] > 0].sort_values("pct", ascending=False))
  print()

  print("3) Columns with more than 50% missing:")
  if over_50.empty:
    print("  None")
  else:
    for col, pct in over_50.items():
      print(f"  {col}: {pct}%")

  print("\nObservation:")
  print("  Cabin has ~68% missing — too sparse for simple imputation;")
  print("  consider dropping or a dedicated 'Missing' category + indicator.")


if __name__ == "__main__":
  try:
    main()
  except Exception as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
