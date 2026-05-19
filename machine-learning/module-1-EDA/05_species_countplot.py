import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    counts = df["species"].value_counts()
    most_common = counts.idxmax()
    print("Species counts:")
    print(counts)
    print(f"\nMost common species: {most_common}")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="species")
    plt.title("Penguin Species Count")
    plt.xlabel("Species")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
