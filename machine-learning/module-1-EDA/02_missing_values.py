import sys

import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    missing = df.isna().sum()
    print("Missing values per column:")
    print(missing)
    print()

    top_column = missing.idxmax()
    top_count = int(missing.max())
    print(f"Highest missing count: {top_column} ({top_count} missing)")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
