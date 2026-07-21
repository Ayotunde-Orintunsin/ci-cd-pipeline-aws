from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "development"
    log_level: str = "INFO"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/tasks"

    class Config:
        env_file = ".env"

settings = Settings()
