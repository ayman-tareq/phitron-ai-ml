import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

DATA_FILE = Path(__file__).with_name("data.csv")


def main() -> None:
  df = pd.read_csv(DATA_FILE)
  train, _ = train_test_split(df, test_size=0.2, random_state=42)

  age_mean = train["Age"].mean()
  age_median = train["Age"].median()

  out = df.copy()
  out["Age_mean_imputed"] = out["Age"].fillna(age_mean)
  out["Age_median_imputed"] = out["Age"].fillna(age_median)

  print("=== Problem 5: Age mean vs median imputation ===\n")
  print(f"Training-only Age mean:   {age_mean:.2f}")
  print(f"Training-only Age median: {age_median:.2f}")
  print(f"Missing Age rows: {df['Age'].isna().sum()}")

  sns.set_theme(style="whitegrid")
  fig, axes = plt.subplots(1, 2, figsize=(12, 4))

  sns.kdeplot(out["Age_mean_imputed"], ax=axes[0], fill=True)
  axes[0].set_title("Age — mean imputed")
  axes[0].set_xlabel("Age")

  sns.kdeplot(out["Age_median_imputed"], ax=axes[1], fill=True)
  axes[1].set_title("Age — median imputed")
  axes[1].set_xlabel("Age")

  plt.tight_layout()
  plt.show()

  print("\nChoice: median imputation")
  print("Observation:")
  print("  Age is often right-skewed (a few very high ages). Mean is pulled")
  print("  toward outliers; median stays near the typical patient and keeps")
  print("  the distribution shape more stable for EDA and many models.")


if __name__ == "__main__":
  try:
    main()
  except Exception as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
