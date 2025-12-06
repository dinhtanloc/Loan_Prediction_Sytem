# model.py
import time
import logging
import numpy as np
import joblib
from fastapi import HTTPException
from prometheus_client import Histogram, Counter
from tracing import trace_span
from .config import PRJ_CFG
logger = logging.getLogger(__name__)

# Prometheus metrics
prediction_duration_histogram = Histogram(
    'ml_prediction_duration_seconds',
    'Time spent on predictions',
    ['endpoint', 'status']
)

error_counter = Counter(
    'ml_errors_total',
    'Total number of errors',
    ['operation', 'error_type']
)


@trace_span("model-loader")
def load_model():
    try:
        model = joblib.load(PRJ_CFG.ml_model_path)
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        error_counter.labels(operation="model_load", error_type=type(e).__name__).inc()
        raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")


@trace_span("predictor")
def make_prediction(model, features):
    start = time.time()

    try:
        if not features:
            raise ValueError("Features cannot be empty")

        features_array = np.array([features])
        prediction = model.predict(features_array)
        result = prediction.tolist()

        prediction_duration_histogram.labels(endpoint="internal", status="success").observe(time.time() - start)
        return result

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        prediction_duration_histogram.labels(endpoint="internal", status="error").observe(time.time() - start)
        error_counter.labels(operation="prediction", error_type=type(e).__name__).inc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
