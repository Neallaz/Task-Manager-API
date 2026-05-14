```markdown
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
- Automated API Testing with pytest
- Alembic Migrations
- Makefile Automation

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
├── tests/
│   └── test_tasks.py
├── alembic/
│   └── versions/
├── Makefile
├── requirements.txt
├── gunicorn_conf.py
├── task_manager_api.service
├── .env.example
├── .gitignore
├── alembic.ini
└── README.md
```

---

# Requirements

- Python 3.11+
- PostgreSQL 15+
- pip
- virtualenv
- make

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Neallaz/Task-Manager-API.git
cd Task-Manager-API
```

## 2. Install with Make

```bash
make install
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Environment Variables

```bash
cp .env.example .env
# Edit .env with your database credentials
```

---

# PostgreSQL Setup

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE tasks_db;
CREATE USER task_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE tasks_db TO task_user;
ALTER DATABASE tasks_db OWNER TO task_user;
\c tasks_db
ALTER SCHEMA public OWNER TO task_user;
GRANT ALL ON SCHEMA public TO task_user;
\q
```

## Example .env

```env
DATABASE_URL=postgresql://task_user:password@localhost:5432/tasks_db
```

---

# Database Migrations

```bash
make migrate
```

Or manually:

```bash
alembic upgrade head
```

---

# Run Application

```bash
make run
```

Or manually:

```bash
uvicorn app.main:app --reload
```

Visit: `http://127.0.0.1:8000/docs`

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks/ | Get all tasks |
| POST | /tasks/ | Create task |
| GET | /tasks/{id} | Get single task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

---

# Request Examples

## Create Task

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
-H "Content-Type: application/json" \
-d '{"title": "Learn FastAPI", "description": "Practice CRUD APIs"}'
```

## Get Tasks

```bash
curl http://127.0.0.1:8000/tasks/
```

## Update Task

```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
-H "Content-Type: application/json" \
-d '{"is_completed": true}'
```

## Delete Task

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

---

# Running Tests

```bash
make test
```

Or manually:

```bash
pytest -v
```

Expected output:

```
===== 5 passed in 0.75s =====
```

---

# Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all commands |
| `make install` | Install dependencies |
| `make run` | Run development server |
| `make test` | Run tests |
| `make migrate` | Run database migrations |
| `make clean` | Clean cache files |
| `make clean-all` | Clean cache + remove venv |
| `make shell` | Open Python shell |

---

# Gunicorn Deployment

```bash
gunicorn app.main:app \
  -k uvicorn.workers.UvicornWorker \
  -b 0.0.0.0:8000 \
  --workers 4
```

---

# systemd Service

```bash
sudo cp task_manager_api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start task_manager_api
sudo systemctl enable task_manager_api
sudo systemctl status task_manager_api
```

## Service File Example

```ini
[Unit]
Description=FastAPI Tasks API
After=network.target postgresql.service

[Service]
User=yourusername
Group=yourgroup
WorkingDirectory=/home/yourusername/Task-Manager-API
Environment="PATH=/home/yourusername/Task-Manager-API/venv/bin"
Environment="DATABASE_URL=postgresql://task_user:password@localhost:5432/tasks_db"
ExecStart=/home/yourusername/Task-Manager-API/venv/bin/gunicorn app.main:app \
    -k uvicorn.workers.UvicornWorker \
    -b 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```


---

# .gitignore

```gitignore
venv/
__pycache__/
.env
*.db
test.db
.pytest_cache/
.vscode/
*.log
```

---

# Technologies Used

- Python / FastAPI
- PostgreSQL / SQLAlchemy
- Alembic / pytest
- Docker / Gunicorn / systemd
- Make

---

Negin Alizadeh
```