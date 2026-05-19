import sys
from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


DATA_FILE = Path(__file__).with_name("data.csv")


def wrong_approach(df: pd.DataFrame) -> None:
  """Fits imputer on full data before split — causes data leakage."""
  imputer = SimpleImputer(strategy="median")
  df[["Age", "Salary"]] = imputer.fit_transform(df[["Age", "Salary"]])
  X = df.drop("Target", axis=1)
  y = df["Target"]
  train_test_split(X, y, test_size=0.2, random_state=42)


def correct_approach(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
  X = df.drop("Target", axis=1)
  y = df["Target"]
  X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
  )

  pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
  ])
  X_train_imp = pipe.fit_transform(X_train[["Age", "Salary"]])
  X_test_imp = pipe.transform(X_test[["Age", "Salary"]])

  return X_train_imp, X_test_imp


def main() -> None:
  if not DATA_FILE.exists():
    raise FileNotFoundError(f"Could not find {DATA_FILE}")
  df = pd.read_csv(DATA_FILE)

  print("=== Problem 1: Data leakage in imputation ===\n")
  print("Issue:")
  print("  The buggy code calls imputer.fit_transform() on the ENTIRE dataset")
  print("  before train_test_split. Test-set values then influence the median")
  print("  used to fill training rows — information from the future leaks in.\n")
  print("Why it is wrong:")
  print("  In real ML, the model must not see test data during preprocessing.")
  print("  Medians (or means) must be learned from training data only.\n")
  print("Fix:")
  print("  1) Split first.")
  print("  2) fit() imputer on X_train only.")
  print("  3) transform() X_train and X_test with those same statistics.")
  print("  Use a Pipeline so this happens automatically in cross-validation.\n")

  X_train_imp, X_test_imp = correct_approach(df.copy())
  print("Corrected run OK.")
  print(f"  Train imputed shape: {X_train_imp.shape}")
  print(f"  Test imputed shape:  {X_test_imp.shape}")
  print("\nObservation: Test medians never enter fit(); evaluation stays honest.")


if __name__ == "__main__":
  try:
    main()
  except Exception as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
