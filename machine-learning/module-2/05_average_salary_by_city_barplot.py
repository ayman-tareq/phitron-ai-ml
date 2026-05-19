import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    df = pd.DataFrame({
        "City": ["Dhaka", "Dhaka", "CTG", "CTG", "Sylhet"],
        "Salary": [50000, 60000, 45000, 55000, 40000],
    })

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(7, 5))
    sns.barplot(data=df, x="City", y="Salary")
    plt.title("Average Salary by City")
    plt.xlabel("City")
    plt.ylabel("Average Salary")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
