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

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_features = np.array(data["features"])  # Accept a list of inputs
    predictions = model.predict(input_features).tolist()  # Predict for all inputs
    confidences = model.predict_proba(input_features).max(axis=1).tolist()  # Get max confidence for each input
    return jsonify({
        "predictions": [int(pred) for pred in predictions],
        "confidences": [round(float(conf), 2) for conf in confidences]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
