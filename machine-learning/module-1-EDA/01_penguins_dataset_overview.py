import sys

import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    rows, cols = df.shape
    print(f"Samples (rows): {rows}")
    print(f"Features (columns): {cols}")
    print()

    print("First 7 rows:")
    print(df.head(7))
    print()

    print("Random sample of 5 rows:")
    print(df.sample(5, random_state=42))
    print()

    print("Observation:")
    print(
        "A random sample shows rows from across the file, not only the start.\n"
        "That helps you spot patterns and outliers that head() alone might hide."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
