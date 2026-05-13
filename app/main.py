from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from app.database import Base, engine
from app.routers import tasks


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manger API",
    description="CRUD API with FastAPI/PostgreSQL",
    version="1.0.0"
)


app.include_router(tasks.router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error"
        }
    )


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": "Tasks API is running"
    }