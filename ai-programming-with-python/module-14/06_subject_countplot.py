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
    if "subject" not in students.columns:
        raise ValueError("Missing column: subject")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=students, x="subject", order=students["subject"].value_counts().index)
    plt.title("Records per Subject")
    plt.xlabel("Subject")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
