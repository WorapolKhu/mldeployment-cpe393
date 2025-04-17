from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Validate that "features" key exists
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request data"}), 400

    # Validate that "features" is a list of lists with exactly 4 float values each
    input_features = data["features"]
    if not isinstance(input_features, list) or not all(isinstance(feature, list) and len(feature) == 4 and all(isinstance(x, (int, float)) for x in feature) for feature in input_features):
        return jsonify({"error": "Invalid input format. 'features' must be a list of lists, each containing exactly 4 numeric values."}), 400

    # Convert input to NumPy array
    input_features = np.array(data["features"])  # Accept a list of inputs
    
    # Predict for all inputs
    predictions = model.predict(input_features).tolist()  # Predict for all inputs
    confidences = model.predict_proba(input_features).max(axis=1).tolist()  # Get max confidence for each input

    # Return predictions and confidences
    return jsonify({
        "predictions": [int(pred) for pred in predictions],
        "confidences": [round(float(conf), 2) for conf in confidences]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
