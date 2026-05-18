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
    required = {"age", "hours_studied", "marks", "attendance_percentage", "previous_gpa", "gender"}
    missing = required - set(students.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    sns.set_theme(style="whitegrid")
    graph = sns.pairplot(
        students,
        vars=["age", "hours_studied", "marks", "attendance_percentage", "previous_gpa"],
        hue="gender",
        corner=True,
    )
    graph.figure.suptitle("Students Pairplot", y=1.02)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
