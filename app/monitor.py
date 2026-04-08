import time
import psutil


def measure_performance(service_function):
    """
    Measures latency, CPU usage, and memory usage
    for a given backend service function.
    """
    start_time = time.time()

    result = service_function()

    end_time = time.time()

    latency_ms = (end_time - start_time) * 1000
    cpu_usage = psutil.cpu_percent(interval=0.1)
    memory_usage = psutil.virtual_memory().percent

    return {
        "result": result,
        "latency_ms": round(latency_ms, 2),
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }