import sys

import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    island_pct = df["island"].value_counts(normalize=True) * 100
    island_pct = island_pct.round(1)

    print("Island percentage distribution:")
    print(island_pct.apply(lambda x: f"{x:.1f}%"))
    print()

    top_island = island_pct.idxmax()
    print(f"Most common island: {top_island} ({island_pct[top_island]:.1f}%)")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
