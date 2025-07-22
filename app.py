from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
from collections import Counter
import matplotlib.pyplot as plt

app = Flask(__name__)

# Updated features list to include 'duration'
expected_features = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes"]

# Load the trained IDS model
model = joblib.load("ids_model.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    predictions = None
    chart_url = None
    total = normal_count = attack_count = 0

    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file and uploaded_file.filename.endswith(".csv"):
            try:
                df = pd.read_csv(uploaded_file)

                #  Check for missing columns
                missing = [col for col in expected_features if col not in df.columns]
                if missing:
                    return f"Error: Missing columns in input CSV: {', '.join(missing)}"

                #  Convert categorical string features into numeric (factorize)
                for col in df.select_dtypes(include=["object"]).columns:
                    df[col] = df[col].astype(str)
                    df[col] = pd.factorize(df[col])[0]

                #  Make predictions
                preds = model.predict(df[expected_features])
                predictions = ["normal" if p == 0 else "attack" for p in preds]

                # Generate summary
                total = len(predictions)
                normal_count = predictions.count("normal")
                attack_count = predictions.count("attack")

                #  Create bar chart
                counts = Counter(predictions)
                plt.figure(figsize=(4, 3))
                plt.bar(counts.keys(), counts.values(), color=["green", "red"])
                plt.title("Prediction Summary")
                plt.xlabel("Type")
                plt.ylabel("Count")
                plt.tight_layout()

                # Save chart to static/
                chart_path = os.path.join("static", "chart.png")
                plt.savefig(chart_path)
                plt.close()
                chart_url = chart_path

            except Exception as e:
                return f"Error during prediction: {e}"

    return render_template("index.html",
                           predictions=predictions,
                           chart_url=chart_url,
                           total=total,
                           normal_count=normal_count,
                           attack_count=attack_count)

if __name__ == "__main__":
    # Create static directory if it doesn't exist
    if not os.path.exists("static"):
        os.makedirs("static")

    app.run(debug=True)


