# 🚚 SmartFleetX

## 🚀 Overview
SmartFleetX is a scalable backend for vehicle fleet tracking and anomaly detection.

## 🔐 Features
- Async REST API with FastAPI
- JWT-based Authentication
- Basic Rate Limiting Middleware
- Background tasks via Celery
- PostgreSQL for data storage
- Redis for Pub/Sub and Celery broker
- Docker Compose setup

## 🛠 Setup
```bash
docker-compose up --build
```

## 🔑 Authentication
Use the `/token` endpoint with:
```bash
curl -X POST http://localhost:8000/token -d "username=admin&password=admin123"
```
Then include the access token in headers:
```
Authorization: Bearer <your_token>
```

## API Docs
http://localhost:8000/docs

## 🧪 Test
```bash
curl -X POST http://localhost:8000/vehicle/telemetry -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"vehicle_id":"V123", "speed":60, "temperature":101, "latitude":12.34, "longitude":56.78}'
```
