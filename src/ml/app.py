import logging

from fastapi import FastAPI

from ml.utils import lifespan

from .api_endpoint import register_routes
from .config import PRJ_CFG

logging.basicConfig(level=PRJ_CFG.ml_log_level)
logger = logging.getLogger(__name__)


app = FastAPI(
    title=PRJ_CFG.ml_service_name,
    version=PRJ_CFG.ml_service_version,
    lifespan=lifespan
)

register_routes(app)


if __name__ == "__main__":
    import uvicorn

    logger.info(
        f"🚀 Starting {PRJ_CFG.ml_service_name} "
        f"v{PRJ_CFG.ml_service_version} on {PRJ_CFG.ml_host}:{PRJ_CFG.ml_port}"
    )

    uvicorn.run(
        app,
        host=PRJ_CFG.ml_host,
        port=int(PRJ_CFG.ml_port)
    )
