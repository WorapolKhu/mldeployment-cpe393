# mldeployment-cpe393

# ML Model Deployment with Flask and Docker

This project demonstrates how to deploy a machine learning model using Flask and Docker. The model is trained on the Iris dataset using a Random Forest Classifier and exposed via a REST API. The API supports predictions with confidence scores and can handle multiple inputs.

---
## Project Description

The project includes:
- A Flask-based API to serve the machine learning model.
- Dockerization for easy deployment.
- Endpoints for health checks and predictions.
- Input validation to ensure robust API behavior.

---
## Setup Steps
1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```sh
   git clone <repository-url>
   cd mldeployment-cpe393
   ```
2. **Train the Model**  
   Run the `train.py` script to train the model and save it as `model.pkl` (model.pkl will be saved in app folder):
   ```sh
   python train.py
   ```
3. **Build the Docker Image**  
   Build the Docker image for the project:
   ```sh
   docker build -t ml-model .
   ```
4. **Run the Docker Container**  
   Start the container and expose the API on port 9000:
   ```sh
   docker run -p 9000:9000 ml-model
   ```
5. **Test the API**  
   Use `curl` or any API testing tool to test the endpoints.

---
## Sample API Request and Response

### Health Check Endpoint
**Request:**
```sh
curl -X GET http://localhost:9000/health
```
**Response:**
```json
{
  "status": "ok"
}
```

---
### Prediction Endpoint
**Request:**
```sh
curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]}'
```

**Response:**
```json
{
  "predictions": [0, 2],
  "confidences": [0.97, 0.85]
}
```

---

# Housing Price Prediction API

This project provides a RESTful API for predicting housing prices using a machine learning model trained on a dataset of house features. The API is built with Flask and serves predictions from a pre-trained model.

## Project Structure

```
Housing/
├── app/
│   ├── app.py              # Flask API for serving predictions
│   ├── model.pkl           # Trained machine learning model (pickle file)
│   └── model_columns.pkl   # List of columns used during model training
├── train.py                # Script for training the model
└── README.md               # Project documentation
```

## Features

- **/ (GET):** Root endpoint to check if the API is running.
- **/health (GET):** Health check endpoint.
- **/predict (POST):** Predict house prices. Accepts JSON input with house features.

---
## Setup Steps

1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```sh
   git clone <repository-url>
   cd mldeployment-cpe393-main/Housing
   ```

2. **Train the Model**  
   Run the `train.py` script to train the model and save `model.pkl` and `model_columns.pkl` in the `app/` directory:
   ```sh
   python train.py
   ```

3. **Run the API**  
   Navigate to the `app/` directory and start the Flask server:
   ```sh
   cd app
   python app.py
   ```
   The API will be available at `http://0.0.0.0:9000/`.

4. **Test the API**  
   Use `curl` or any API testing tool to test the endpoints.

   **Health Check Example:**
   ```sh
   curl -X GET http://localhost:9000/health
   ```

   **Prediction Example:**
   ```sh
   curl -X POST http://localhost:9000/predict \
        -H "Content-Type: application/json" \
        -d '{"features": [{"area": 7420, "bedrooms": 4, "bathrooms": 2, "stories": 3, "mainroad": "yes", "guestroom": "no", "basement": "yes", "hotwaterheating": "no", "airconditioning": "yes", "parking": 2, "prefarea": "yes", "furnishingstatus": "furnished"}]}'
   ```
   **Example response:**
   ```json
   {
   "predictions": [133000.0]
   }
   ```