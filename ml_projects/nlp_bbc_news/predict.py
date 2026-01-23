import argparse
import os
import joblib
import pandas as pd


def parse_args():
    p = argparse.ArgumentParser(description="BBC News Text Classification - Batch Prediction")
    p.add_argument("--input", required=True, help="Path to input CSV containing a text column")
    p.add_argument("--text_col", default="text", help="Name of text column in input CSV (default: text)")
    p.add_argument("--model", default="ml_projects/nlp_bbc_news/models/bbc_news_linear_svc_pipeline.joblib",
                   help="Path to saved sklearn pipeline joblib")
    p.add_argument("--output", default="ml_projects/nlp_bbc_news/predictions.csv",
                   help="Path to output CSV with predictions")
    return p.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.model):
        raise FileNotFoundError(f"Model not found: {args.model}")

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found: {args.input}")

    df = pd.read_csv(args.input)

    if args.text_col not in df.columns:
        raise ValueError(
            f"Column '{args.text_col}' not found in input CSV. Available columns: {list(df.columns)}"
        )

    model = joblib.load(args.model)

    texts = df[args.text_col].astype(str)
    preds = model.predict(texts)

    out = df.copy()
    out["predicted_category"] = preds
    out.to_csv(args.output, index=False)

    print("Saved predictions to:", args.output)
    print("Prediction counts:")
    print(out["predicted_category"].value_counts())


if __name__ == "__main__":
    main()
