from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str= "postgresql://task_user:password@localhost:5432/taskdb"
    class Config:
        env_file = ".env"


settings = Settings()