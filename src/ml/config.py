# config/config.py
import os

import yaml
from dotenv import find_dotenv, load_dotenv
from pyprojroot import here

load_dotenv(find_dotenv())

with open(here("config/project_config.yml")) as cfg:
    app_config = yaml.load(cfg, Loader=yaml.FullLoader)


class LoadProjectConfig:
    def __init__(self):
        self.ml = app_config.get("ml", {})

        service = self.ml["service"]
        self.ml_service_name = service["name"]
        self.ml_service_version = service["version"]
        self.ml_host = service["host"]
        self.ml_port = service["port"]
        self.ml_base_url = service["base_url"]

        os.environ["ML_SERVICE_NAME"] = self.ml_service_name
        os.environ["ML_SERVICE_PORT"] = str(self.ml_port)
        os.environ["ML_SERVICE_BASE_URL"] = self.ml_base_url


        self.ml_model_path = here(self.ml["model"]["path"])
        self.ml_memory_dir = here(self.ml["memory"]["directory"])


        monitor = self.ml["monitoring"]
        self.ml_tracing_enabled = monitor["tracing_enabled"]
        self.ml_jaeger_host = monitor["jaeger_host"]
        self.ml_jaeger_port = monitor["jaeger_port"]

        os.environ["ML_JAEGER_HOST"] = self.ml_jaeger_host
        os.environ["ML_JAEGER_PORT"] = str(self.ml_jaeger_port)

 
        prom = self.ml["prometheus"]
        self.ml_prometheus_enabled = prom["enabled"]
        self.ml_metrics_path = prom["metrics_path"]

        log_cfg = self.ml["logging"]
        self.ml_log_level = log_cfg["level"]
        self.ml_json_log = log_cfg["json_format"]

        self.mongodb_uri = os.getenv("MONGODB_URL")
        self.gcp_project_id = os.getenv("GCP_PROJECT_ID")

        if not self.mongodb_uri:
            print("[WARN] MONGODB_URL not found in .env")
        if not self.gcp_project_id:
            print("[WARN] GCP_PROJECT_ID not found in .env")


PRJ_CFG = LoadProjectConfig()
