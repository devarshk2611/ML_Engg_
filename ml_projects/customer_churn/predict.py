import pandas as pd
import joblib
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Customer Churn Prediction")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", default="predictions.csv", help="Output CSV file")
    parser.add_argument("--model", default="models/customer_churn_rf.joblib", help="Trained model path")
    args = parser.parse_args()

    # Load model
    model = joblib.load(args.model)

    # Load data
    df = pd.read_csv(args.input)
    # If target column exists in the input (common when using training data), drop it for inference
    for target in ["Churn", "churn"]:
    	if target in df.columns:
        	df = df.drop(columns=[target])


    # Predict
    predictions = model.predict(df)
    df["churn_prediction"] = predictions

    # Save predictions
    df.to_csv(args.output, index=False)
    print(f"Predictions saved to {args.output}")

if __name__ == "__main__":
    main()
