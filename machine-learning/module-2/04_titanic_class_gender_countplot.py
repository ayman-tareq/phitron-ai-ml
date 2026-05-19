import sys

import matplotlib.pyplot as plt
import seaborn as sns


def main() -> None:
    df = sns.load_dataset("titanic")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="pclass", hue="sex")
    plt.title("Passenger Class by Gender")
    plt.xlabel("Passenger Class")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
