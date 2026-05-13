from fastapi import FastAPI

from app.database import Base, engine
from app.routers import tasks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tasks API",
    description="Task Manger API with FastAPI and PostgreSQL",
)


app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Tasks API is running"}