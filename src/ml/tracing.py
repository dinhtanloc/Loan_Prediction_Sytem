import logging
from functools import wraps

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

from .config import PRJ_CFG

logger = logging.getLogger(__name__)

if not PRJ_CFG.ml_tracing_enabled:
    logger.warning("Tracing is DISABLED via project_config.yml")

    def trace_span(span_name):
        """No-op decorator when tracing disabled."""
        def decorator(func):
            return func
        return decorator

    tracer = None


else:
    set_tracer_provider(
        TracerProvider(
            resource=Resource.create({
                SERVICE_NAME: PRJ_CFG.ml_service_name
            })
        )
    )

    jaeger_exporter = JaegerExporter(
        agent_host_name=PRJ_CFG.ml_jaeger_host,
        agent_port=int(PRJ_CFG.ml_jaeger_port),
    )

    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(jaeger_exporter)
    )

    tracer = get_tracer_provider().get_tracer(
        PRJ_CFG.ml_service_name,
        PRJ_CFG.ml_service_version,
    )

    logger.info(
        f"[Tracing] Initialized → {PRJ_CFG.ml_service_name} v{PRJ_CFG.ml_service_version} "
        f"→ Jaeger {PRJ_CFG.ml_jaeger_host}:{PRJ_CFG.ml_jaeger_port}"
    )


    def trace_span(span_name):
        """Decorator for auto-tracing."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                with tracer.start_as_current_span(span_name) as span:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        span.record_exception(e)
                        span.set_status(
                            trace.Status(
                                trace.StatusCode.ERROR,
                                str(e)
                            )
                        )
                        raise
            return wrapper
        return decorator
