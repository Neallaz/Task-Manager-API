# FastAPI Tasks API

A simple CRUD REST API built with FastAPI and PostgreSQL.

---

# Features

- FastAPI Framework
- PostgreSQL Database
- Full CRUD Operations
- Swagger Documentation
- Docker Support
- Gunicorn Deployment
- systemd Service
- Linux Ready

---

# Project Structure

```bash
project/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── config.py
│   ├── routers/
│   │   └── tasks.py
│   └── __init__.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── gunicorn_conf.py
├── taskapi.service
├── .env
├── .gitignore
└── README.md
```

---

# Requirements

- Python 3.11+
- PostgreSQL
- pip
- virtualenv

---

# Installation

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL

cd project
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Login to PostgreSQL:

```bash
sudo -u postgres psql
```

Create database and user:

```sql
CREATE DATABASE tasks_db;

CREATE USER postgres WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE tasks_db TO task_user;
```

Exit:

```sql
\q
```

---

# Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/tasks_db
```

---

# Run Application

## Development Mode

```bash
uvicorn app.main:app --reload
```

Application runs on:

```bash
http://127.0.0.1:8000
```

---

# Swagger Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks/ | Get all tasks |
| POST | /tasks/ | Create new task |
| GET | /tasks/{task_id} | Get single task |
| PUT | /tasks/{task_id} | Update task |
| DELETE | /tasks/{task_id} | Delete task |

---

# Request Examples

## Create Task

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Learn FastAPI",
  "description": "Practice CRUD APIs"
}'
```

---

## Get Tasks

```bash
curl http://127.0.0.1:8000/tasks/
```

---

## Update Task

```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
-H "Content-Type: application/json" \
-d '{
  "is_completed": true
}'
```

---

## Delete Task

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

---

# Docker Setup

## Build and Run

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

Swagger URL:

```bash
http://localhost:8000/docs
```

---

# Gunicorn Deployment

Run with Gunicorn:

```bash
gunicorn app.main:app \
-k uvicorn.workers.UvicornWorker \
-b 0.0.0.0:8000
```

---

# systemd Service

Copy service file:

```bash
sudo cp taskapi.service /etc/systemd/system/
```

Reload daemon:

```bash
sudo systemctl daemon-reload
```

Start service:

```bash
sudo systemctl start taskapi
```

Enable auto start:

```bash
sudo systemctl enable taskapi
```

Check status:

```bash
sudo systemctl status taskapi
```

---

# Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Gunicorn
- Uvicorn
- Docker
- systemd

---

Negin Alizadeh
