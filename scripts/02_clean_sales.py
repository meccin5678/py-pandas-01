from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/sales_dirty.csv")
CLEAN_DATA_PATH = Path("data/processed/sales_clean.csv")


def main() -> None:
    df = pd.read_csv(RAW_DATA_PATH)
    df_clean = df.copy()

    df_clean["region"] = df_clean["region"].fillna("Unknown")
    df_clean["region"] = df_clean["region"].str.strip()
    df_clean["region"] = df_clean["region"].replace(
        {
            "大阪": "Osaka",
            "Osaka": "Osaka",
            "Tokyo": "Tokyo",
            "tokyo": "Tokyo",
            "Nagoya": "Nagoya",
            "Unknown": "Unknown",
        }
    )

    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"元データ: {RAW_DATA_PATH}")
    print(f"作成ファイル: {CLEAN_DATA_PATH}")
    print("\n地域の件数:")
    print(df_clean["region"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
