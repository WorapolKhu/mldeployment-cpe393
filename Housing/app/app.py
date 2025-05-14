from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load columns used during training
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Validate input
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request data"}), 400

    input_data = data["features"]
    if not isinstance(input_data, list) or not all(isinstance(item, dict) for item in input_data):
        return jsonify({"error": "Invalid input format. 'features' must be a list of dictionaries."}), 400

    # Convert to DataFrame
    input_df = pd.DataFrame(input_data)

    # Preprocess categorical variables (must match training)
    categorical_cols = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]
    input_df = pd.get_dummies(input_df, columns=categorical_cols)

    # Align columns with training data
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict
    predictions = model.predict(input_df).tolist()

    return jsonify({
        "predictions": [round(float(pred), 2) for pred in predictions]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
