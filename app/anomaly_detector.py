import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies():
    file_path = "data/performance_logs.csv"

    df = pd.read_csv(file_path)

    print(df.columns)

    features = df[df.columns[1:4]] 

    model = IsolationForest(contamination=0.2, random_state=42)

    df["anomaly"] = model.fit_predict(features)

    anomalies = df[df["anomaly"] == -1]

    return anomalies