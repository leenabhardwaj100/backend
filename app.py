import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model_train import train_model

# Initialize FastAPI app
app = FastAPI(title="Iris Prediction API")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to store model data
model_data = None

def get_model():
    """Load model.pkl or train it if it doesn't exist."""
    global model_data
    if not os.path.exists('model.pkl'):
        print("model.pkl not found. Training model now...")
        train_model()
    
    if model_data is None:
        model_data = joblib.load('model.pkl')
    return model_data

@app.on_event("startup")
async def startup_event():
    """Ensure model is loaded on startup."""
    get_model()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API. Use /predict (POST) to get predictions."}

@app.post("/predict")
async def predict(input_data: IrisInput):
    """
    Predict the iris species based on input features.
    """
    try:
        data = get_model()
        model = data['model']
        target_names = data['target_names']
        
        # Prepare input for prediction
        features = np.array([[
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]])
        
        # Get prediction and probabilities
        prediction_idx = model.predict(features)[0]
        prediction_label = target_names[prediction_idx]
        
        # Confidence score (probability of the predicted class)
        probabilities = model.predict_proba(features)[0]
        confidence = float(probabilities[prediction_idx])
        
        return {
            "prediction": prediction_label,
            "confidence": confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Use port 3000 as per environment constraints for internal testing if needed
    # but the deployment command uses $PORT.
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
