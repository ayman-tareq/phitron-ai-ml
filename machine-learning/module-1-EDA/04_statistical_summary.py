import sys

import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    print("DataFrame info (types and non-null counts):")
    df.info()
    print()

    print("Statistical summary for numerical columns:")
    print(df.describe())
    print()

    max_mass = df["body_mass_g"].max()
    mean_flipper = df["flipper_length_mm"].mean()
    print(f"Maximum body_mass_g: {max_mass}")
    print(f"Mean flipper_length_mm: {mean_flipper:.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
