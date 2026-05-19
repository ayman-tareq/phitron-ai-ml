import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("penguins")

    sex_counts = df["sex"].value_counts()
    print("Sex value counts:")
    print(sex_counts)
    print()

    labels = sex_counts.index.tolist()
    sizes = sex_counts.values

    plt.figure(figsize=(7, 7))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Penguin Sex Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
