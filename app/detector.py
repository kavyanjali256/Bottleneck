def detect_bottleneck(service_name, metrics):
    """
    Detects if a service is a performance bottleneck
    based on latency threshold.
    """
    latency_threshold = 500   # milliseconds

    if metrics["latency_ms"] > latency_threshold:
        return f"🚨 Bottleneck detected in {service_name}"

    return f"✅ {service_name} running normally"