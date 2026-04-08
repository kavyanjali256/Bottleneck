def analyze_root_cause(metrics):
    latency = metrics["latency_ms"]
    cpu = metrics["cpu_usage"]
    memory = metrics["memory_usage"]

    if latency > 1000:
        if cpu > 70:
            return "High CPU usage causing service slowdown"
        elif memory > 80:
            return "High memory usage / possible memory leak"
        else:
            return "Possible database query or network I/O delay"

    elif latency > 500:
        return "Moderate latency spike detected"

    else:
        return "System healthy"


from service import (
    feed_service,
    profile_service,
    recommendation_service
)

from monitor import measure_performance
from detector import detect_bottleneck
from logger import log_metrics
from anomaly_detector import detect_anomalies


services = {
    "Feed Service": feed_service,
    "Profile Service": profile_service,
    "Recommendation Service": recommendation_service
}


print("===== Backend Performance Analysis =====\n")

for service_name, service_function in services.items():
    metrics = measure_performance(service_function)

    print(f"Service: {service_name}")
    print(metrics)

    status = detect_bottleneck(service_name, metrics)
    print(status)

    print("Root Cause:", analyze_root_cause(metrics))

    log_metrics(service_name, metrics)

    print("-" * 50)


print("\n===== AI-Based Anomaly Detection Results =====")
print(detect_anomalies())