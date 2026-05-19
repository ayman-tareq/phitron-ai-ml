import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    df = pd.DataFrame({
        "Height": [150, 160, 170, 175, 180],
        "Weight": [50, 60, 70, 75, 80],
    })

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x="Height", y="Weight")
    plt.title("Height vs Weight")
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
