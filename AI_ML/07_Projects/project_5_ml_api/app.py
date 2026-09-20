"""
ML Model as an API — FastAPI Application
=========================================

Serve ML predictions through a REST API.

Usage:
    uvicorn app:app --reload --port 8000

API docs:
    http://localhost:8000/docs
"""

from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os


# =============================================================================
# Configuration
# =============================================================================

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.joblib")
MODEL_VERSION = "1.0.0"


# =============================================================================
# Pydantic Models (Request/Response Schemas)
# =============================================================================

class PredictionRequest(BaseModel):
    """Input features for prediction.

    TODO: Customize these fields to match your model's features.
    Example below is for the house price predictor.
    """
    features: list[float] = Field(
        ...,
        description="List of input feature values",
        min_length=1,
        example=[8.3252, 41.0, 6.98, 1.02, 322.0, 2.56, 37.88, -122.23]
    )


class PredictionResponse(BaseModel):
    """Prediction result."""
    prediction: float = Field(..., description="Model prediction value")
    model_version: str = Field(..., description="Version of the model used")
    timestamp: str = Field(..., description="Prediction timestamp (ISO format)")


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    model_loaded: bool
    model_version: str
    timestamp: str


class ErrorResponse(BaseModel):
    """Error response."""
    error: str
    detail: str


# =============================================================================
# App Setup
# =============================================================================

app = FastAPI(
    title="ML Prediction API",
    description="Serve ML model predictions via REST API",
    version=MODEL_VERSION,
)

model = None


# =============================================================================
# Model Loading
# =============================================================================

def load_model():
    """Load the ML model from disk at startup.

    Returns:
        Loaded model object, or None if loading fails.

    TODO:
        - Update MODEL_PATH to point to your saved model
        - For PyTorch models, use torch.load() instead of joblib
    """
    pass


@app.on_event("startup")
async def startup_event():
    """Load the model when the API starts."""
    global model
    model = load_model()
    if model is not None:
        print(f"✅ Model loaded from {MODEL_PATH}")
    else:
        print(f"⚠️  Model not found at {MODEL_PATH} — /predict will return errors")


# =============================================================================
# Endpoints
# =============================================================================

@app.get("/")
async def root():
    """Welcome endpoint.

    Returns:
        dict: Welcome message with links to docs.
    """
    return {
        "message": "ML Prediction API",
        "docs": "/docs",
        "health": "/health",
        "predict": "POST /predict"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint.

    Returns:
        HealthResponse: API and model status.

    TODO:
        - Add more checks: disk space, memory usage, etc.
    """
    pass


@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make a prediction with the loaded model.

    Args:
        request (PredictionRequest): Input features.

    Returns:
        PredictionResponse: Prediction result.

    Raises:
        HTTPException(503): If model is not loaded.
        HTTPException(400): If input is invalid.
        HTTPException(500): If prediction fails.

    TODO:
        - Add preprocessing if your model expects scaled/encoded input
        - Add input validation specific to your model
        - Add logging for monitoring
    """
    pass


# =============================================================================
# Additional Endpoints (Optional)
# =============================================================================

@app.post("/predict/batch")
async def predict_batch(requests: list[PredictionRequest]):
    """Make batch predictions.

    Args:
        requests (list[PredictionRequest]): Multiple prediction requests.

    Returns:
        list[PredictionResponse]: Predictions for each input.

    TODO: Implement batch prediction for efficiency.
    """
    pass


@app.get("/model/info")
async def model_info():
    """Return model metadata.

    Returns:
        dict: Model type, version, features, etc.

    TODO: Customize with your model's details.
    """
    return {
        "model_version": MODEL_VERSION,
        "model_path": MODEL_PATH,
        "model_loaded": model is not None,
        "model_type": type(model).__name__ if model else None,
    }
