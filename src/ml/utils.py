import logging
from contextlib import asynccontextmanager
from prometheus_client import Counter

from model import load_model

logger = logging.getLogger(__name__)

# Prometheus request counter
model_request_counter = Counter(
    'model_request_total',
    'Total number of requests sent to model',
    ['endpoint']
)

cached_model = None


@asynccontextmanager
async def lifespan(app):
    global cached_model
    logger.info("Service starting...")

    try:
        cached_model = load_model()
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Startup model load failed: {e}")

    yield

    logger.info("Shutting down service...")
    cached_model = None
