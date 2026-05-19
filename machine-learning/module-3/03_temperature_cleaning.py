import sys
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).with_name("data.csv")


def clean_temperature(series: pd.Series) -> pd.Series:
  cleaned = series.replace("Unknown", pd.NA)
  return pd.to_numeric(cleaned, errors="coerce")


def main() -> None:
  df = pd.read_csv(DATA_FILE)

  print("=== Problem 3: Temperature cleaning ===\n")
  print("Before cleaning:")
  print(f"  dtype: {df['Temperature'].dtype}")
  print(f"  'Unknown' count: {(df['Temperature'] == 'Unknown').sum()}")
  print(f"  NaN count: {df['Temperature'].isna().sum()}")

  df["Temperature_clean"] = clean_temperature(df["Temperature"])

  print("\nAfter cleaning (numeric):")
  print(f"  dtype: {df['Temperature_clean'].dtype}")
  print(f"  NaN count (Unknown + original NaN): {df['Temperature_clean'].isna().sum()}")
  print(f"  min: {df['Temperature_clean'].min():.1f}, max: {df['Temperature_clean'].max():.1f}")
  print(f"  mean: {df['Temperature_clean'].mean():.2f}")

  print("\nSteps applied:")
  print("  1) Replace string 'Unknown' with NA")
  print("  2) Convert to numeric (invalid strings → NaN)")
  print("  3) Then impute (median/mean) in a Pipeline fit on train only")

  print("\nObservation:")
  print("  Mixed types must be cleaned before SimpleImputer; otherwise")
  print("  sklearn cannot compute median on text values.")


if __name__ == "__main__":
  try:
    main()
  except Exception as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
