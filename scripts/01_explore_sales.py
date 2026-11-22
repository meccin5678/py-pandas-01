from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


DATA_PATH = Path("data/processed/sales_clean.csv")


def main() -> None:
    rcParams["font.family"] = "Hiragino Sans"

    df = pd.read_csv(DATA_PATH)

    print("=== Data shape ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n=== Column information ===")
    print(df.dtypes)

    print("\n=== Missing values ===")
    missing_summary = pd.DataFrame(
        {
            "missing_count": df.isna().sum(),
            "missing_ratio": df.isna().mean().mul(100).round(2),
        }
    )
    print(missing_summary)

    print("\n=== Rows containing missing values ===")
    print(df[df.isna().any(axis=1)].to_string(index=False))

    print("\n=== Duplicate rows ===")
    print(f"Duplicate count: {df.duplicated().sum()}")
    print(df[df.duplicated(keep=False)].to_string(index=False))

    region_counts = df["region"].value_counts(dropna=False).sort_values(ascending=True)

    plt.figure(figsize=(8, 5))
    region_counts.plot(kind="barh")
    plt.title("Record count by region")
    plt.xlabel("Count")
    plt.ylabel("Region")
    plt.tight_layout()

    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    output_path = report_dir / "region_record_count.png"
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"\nChart saved: {output_path}")


if __name__ == "__main__":
    main()
