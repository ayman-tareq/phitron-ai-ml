import sys

import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    duplicate_count = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_count}")

    df_clean = df.drop_duplicates()
    print(f"Rows before: {len(df)}")
    print(f"Rows after removing duplicates: {len(df_clean)}")

    if duplicate_count == 0:
        print("Observation: No duplicate rows were found in this dataset.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
