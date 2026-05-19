import sys
from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer

DATA_FILE = Path(__file__).with_name("data.csv")


def main() -> None:
  df = pd.read_csv(DATA_FILE)

  print("=== Problem 4: Diagnosis imputation ===\n")
  print(f"Missing Diagnosis before: {df['Diagnosis'].isna().sum()}")

  df["Diagnosis_missing"] = df["Diagnosis"].isna().astype(int)

  imputer = SimpleImputer(strategy="constant", fill_value="Missing")
  df["Diagnosis"] = imputer.fit_transform(df[["Diagnosis"]]).ravel()

  print(f"Missing Diagnosis after:  {df['Diagnosis'].isna().sum()}")
  print(f"Rows flagged by indicator: {df['Diagnosis_missing'].sum()}")
  print("\nValue counts (top):")
  print(df["Diagnosis"].value_counts().head())

  print("\nObservation:")
  print("  Constant fill keeps a valid category for models that need strings.")
  print("  The indicator column preserves the fact that the value was missing.")


if __name__ == "__main__":
  try:
    main()
  except Exception as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
