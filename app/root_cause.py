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