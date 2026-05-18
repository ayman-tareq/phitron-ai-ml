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
    required = {"hours_studied", "marks", "gender"}
    missing = required - set(students.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=students, x="hours_studied", y="marks", hue="gender", s=80)
    plt.title("Study Hours vs Marks by Gender")
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
