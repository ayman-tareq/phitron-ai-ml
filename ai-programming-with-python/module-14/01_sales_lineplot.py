from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_FILE = Path(__file__).with_name("sales.csv")


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE.name}")

    sales = pd.read_csv(DATA_FILE)
    missing = {"date", "sales"} - set(sales.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    sales["date"] = pd.to_datetime(sales["date"])

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(11, 5))
    sns.lineplot(data=sales, x="date", y="sales", marker="o")
    plt.title("Daily Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
