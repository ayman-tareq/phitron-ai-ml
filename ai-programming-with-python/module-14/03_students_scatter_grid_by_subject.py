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
    required = {"hours_studied", "marks", "subject"}
    missing = required - set(students.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    sns.set_theme(style="whitegrid")
    grid = sns.relplot(
        data=students,
        x="hours_studied",
        y="marks",
        col="subject",
        kind="scatter",
        height=4,
        aspect=1,
    )
    grid.set_axis_labels("Hours Studied", "Marks")
    grid.set_titles("Subject: {col_name}")
    grid.figure.suptitle("Study Hours vs Marks by Subject", y=1.05)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
