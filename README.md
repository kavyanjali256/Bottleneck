# AI-Based Performance Bottleneck Detection System  
### LinkedIn Backend Case Study

## Overview
This project focuses on detecting **performance bottlenecks in distributed backend services** using LinkedIn as a case study.

Modern platforms like LinkedIn rely on multiple backend services such as:
- Feed Service
- Profile Service
- Recommendation Engine
- Database Layer
- Cache Layer

If any one of these services becomes slow, the overall response time of the application increases.

This project simulates such backend services and automatically identifies the bottleneck using performance metrics like:
- latency
- CPU usage
- memory usage
- response time

---

## Problem Statement
To design a backend system that can **monitor service performance and automatically detect bottlenecks** in a distributed architecture similar to LinkedIn.

---

## Objectives
- Simulate backend services
- Measure service latency
- Detect slow services
- Log performance metrics
- Analyze root cause of delays
- Build an AI-based anomaly detection system

---

## Tech Stack
- Python
- Flask / FastAPI
- psutil
- pandas
- scikit-learn
- CSV / SQLite

---

## Project Structure
```text
linkedin-bottleneck-detector/
│
├── app/
│   ├── main.py
│   ├── services.py
│   ├── monitor.py
│   ├── detector.py
│   ├── logger.py
│   └── database.py
│
├── data/
│   └── performance_logs.csv
│
├── requirements.txt
└── README.md
