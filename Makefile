# Makefile for Task Manager API

.PHONY: help install run test migrate docker-up docker-down clean

# Colors
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m

help:
	@echo "$(GREEN)Available commands:$(NC)"
	@echo "  make install     - Install dependencies"
	@echo "  make run         - Run development server"
	@echo "  make test        - Run tests"
	@echo "  make migrate     - Run database migrations"
	@echo "  make clean       - Clean cache files"

install:
	@echo "$(GREEN)Installing dependencies...$(NC)"
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	@echo "$(GREEN)Done! Activate with: source venv/bin/activate$(NC)"

run:
	@echo "$(GREEN)Starting development server...$(NC)"
	. venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	@echo "$(GREEN)Running tests...$(NC)"
	. venv/bin/activate && pytest tests/test_tasks.py -v

test-cov:
	@echo "$(GREEN)Running tests with coverage...$(NC)"
	. venv/bin/activate && pytest tests/test_tasks.py --cov=app -v

migrate:
	@echo "$(GREEN)Running database migrations...$(NC)"
	. venv/bin/activate && alembic upgrade head

migrate-new:
	@echo "$(GREEN)Creating new migration...$(NC)"
	@read -p "Migration message: " msg; \
	. venv/bin/activate && alembic revision --autogenerate -m "$$msg"

migrate-down:
	@echo "$(GREEN)Rollback last migration...$(NC)"
	. venv/bin/activate && alembic downgrade -1

docker-up:
	@echo "$(GREEN)Starting Docker containers...$(NC)"
	docker compose up --build -d
	@echo "$(GREEN)Containers started!$(NC)"

docker-down:
	@echo "$(GREEN)Stopping Docker containers...$(NC)"
	docker compose down

logs:
	docker compose logs -f

shell:
	@echo "$(GREEN)Opening Python shell...$(NC)"
	. venv/bin/activate && python

clean:
	@echo "$(GREEN)Cleaning cache files...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/ .coverage htmlcov/
	@echo "$(GREEN)Clean complete!$(NC)"

clean-all: clean
	@echo "$(GREEN)Removing virtual environment...$(NC)"
	rm -rf venv/
	rm -f test.db
	@echo "$(GREEN)All cleaned!$(NC)"

db-reset:
	@echo "$(RED)WARNING: This will delete all data!$(NC)"
	@read -p "Are you sure? (y/N): " confirm; \
	if [ "$$confirm" = "y" ]; then \
		psql -U task_user -d tasks_db -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"; \
		. venv/bin/activate && alembic upgrade head; \
		echo "$(GREEN)Database reset complete!$(NC)"; \
	else \
		echo "Cancelled."; \
	fi

.PHONY: help install run test test-cov migrate migrate-new migrate-down docker-up docker-down logs shell clean clean-all db-reset