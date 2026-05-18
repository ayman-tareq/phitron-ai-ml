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
    if "hours_studied" not in students.columns:
        raise ValueError("Missing column: hours_studied")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=students, x="hours_studied", fill=True)
    plt.title("KDE Curve of Hours Studied")
    plt.xlabel("Hours Studied")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
