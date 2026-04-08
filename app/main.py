from logger import log_metrics
from service import (
    feed_service,
    profile_service,
    recommendation_service
)

from monitor import measure_performance
from detector import detect_bottleneck


services = {
    "Feed Service": feed_service,
    "Profile Service": profile_service,
    "Recommendation Service": recommendation_service
}


for service_name, service_function in services.items():
    metrics = measure_performance(service_function)

    print(service_name)
    print(metrics)
    

    status = detect_bottleneck(service_name, metrics)
    print(status)
    log_metrics(service_name, metrics)


    print("-" * 40)


print("\nAI-Based Anomaly Detection Results")
print(detect_anomalies())    