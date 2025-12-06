# api_endpoint.py
import time
import logging
from fastapi import HTTPException
from fastapi.responses import Response
from typing import List

from tracing import tracer
from model import load_model, make_prediction
from ml.utils import model_request_counter
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Histogram

logger = logging.getLogger(__name__)

# Histogram cho endpoint
endpoint_histogram = Histogram(
    'ml_prediction_endpoint_seconds',
    'Time spent processing prediction endpoint',
    ['status']
)


def register_routes(app):
    @app.post("/predict")
    def predict(features: List[float]):
        model_request_counter.labels(endpoint="/predict").inc()
        start = time.time()

        try:
            with tracer.start_as_current_span("prediction-endpoint") as span:
                logger.info(f"Request features: {features}")

                model = load_model()
                prediction = make_prediction(model, features)

                span.set_attribute("prediction.result", str(prediction))
                endpoint_histogram.labels(status="success").observe(time.time() - start)

                return {"prediction": prediction, "status": "success"}

        except HTTPException as he:
            endpoint_histogram.labels(status="http_error").observe(time.time() - start)
            raise he

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            endpoint_histogram.labels(status="error").observe(time.time() - start)
            raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

    @app.get("/metrics")
    def metrics():
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

    @app.get("/")
    def root():
        return {"message": "ML Prediction Service is running"}

    @app.get("/health")
    def health():
        try:
            load_model()
            return {"status": "healthy", "model_loaded": True}
        except:
            return {"status": "unhealthy", "model_loaded": False}
