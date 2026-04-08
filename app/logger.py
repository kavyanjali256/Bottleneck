import csv
import os


def log_metrics(service_name, metrics):
    file_path = "data/performance_logs.csv"

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "service_name",
                "latency_ms",
                "cpu_usage",
                "memory_usage"
            ])

        writer.writerow([
            service_name,
            metrics["latency_ms"],
            metrics["cpu_usage"],
            metrics["memory_usage"]
        ])