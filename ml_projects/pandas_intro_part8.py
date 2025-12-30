# ml_projects/predict.py
"""
CLI inference script for the Iris project.
- Loads the best trained model (joblib)
- Reads an input CSV of samples
- Outputs predictions to stdout or a CSV

Assumptions:
- The model was trained on columns from `ml_projects/data/iris_cleaned_engineered.csv`
  with features X = df.drop(columns=['species','species_index']).
- So inputs should contain the same feature columns (order-insensitive; we align them).

Usage:
  python ml_projects/predict.py --model ml_projects/models/best_model.joblib \
                                --input ml_projects/data/iris_cleaned_engineered.csv \
                                --output ml_projects/preds.csv
"""
import argparse
import joblib
import pandas as pd
from pathlib import Path

DEF_MODEL = "ml_projects/models/best_model.joblib"
DEF_TRAIN = "ml_projects/data/iris_cleaned_engineered.csv"

def get_feature_columns_from_train(train_path: str):
    df_train = pd.read_csv(train_path)
    feat_cols = [c for c in df_train.columns if c not in ("species", "species_index")]
    return feat_cols

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEF_MODEL, help="Path to .joblib model")
    ap.add_argument("--input", required=True, help="Path to input CSV with feature columns")
    ap.add_argument("--output", default="", help="Optional path to save predictions CSV")
    ap.add_argument("--train_header", default=DEF_TRAIN, help="CSV to read feature columns from")
    args = ap.parse_args()

    model = joblib.load(args.model)

    # Derive the feature column order from the training CSV
    feat_cols = get_feature_columns_from_train(args.train_header)

    df = pd.read_csv(args.input)

    # Drop target columns if present in input
    for col in ("species", "species_index"):
        if col in df.columns:
            df = df.drop(columns=[col])

    # Align/validate columns
    missing = [c for c in feat_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Input is missing required columns: {missing}")

    X = df[feat_cols]  # order columns exactly as during training
    preds = model.predict(X)

    out_df = df.copy()
    out_df["predicted_species"] = preds

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        out_df.to_csv(args.output, index=False)
        print(f"Saved predictions to: {args.output}")
    else:
        # Print a small preview to stdout if no output path
        print(out_df.head(10).to_string(index=False))

if __name__ == "__main__":
    main()