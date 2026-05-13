from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing create"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["is_completed"] is False


def test_get_tasks():
    response = client.get("/tasks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_task():
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Single Task",
            "description": "Testing single task"
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Old Title",
            "description": "Old Description"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Title",
            "is_completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Title"
    assert data["is_completed"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Delete Task",
            "description": "Delete Test"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
