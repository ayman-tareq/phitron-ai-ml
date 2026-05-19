import sys
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).with_name("data.csv")
REPORT_FILE = Path(__file__).with_name("eda_report.html")


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE.name}")

    try:
        from ydata_profiling import ProfileReport
    except ImportError as error:
        raise ImportError(
            "Install ydata-profiling: pip install ydata-profiling "
            "(Python 3.10–3.13 recommended; 3.14 support is still rolling out)"
        ) from error

    df = pd.read_csv(DATA_FILE)
    profile = ProfileReport(df, title="EDA Report")
    profile.to_file(REPORT_FILE)

    print(f"Report saved: {REPORT_FILE}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
