from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_FILE = Path(__file__).with_name("students.csv")


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE.name}")

    students = pd.read_csv(DATA_FILE)
    if "marks" not in students.columns:
        raise ValueError("Missing column: marks")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.histplot(data=students, x="marks", kde=True, bins=12)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
