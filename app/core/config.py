from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TITLE: str = "Название проекта"
    DATABASE_URL: str = "sqlite+aiosqlite:///./fastapi.db"

    DEPOSIT: str = "DEPOSIT"
    WITHDRAW: str = "WITHDRAW"

    class Config:
        env_file = ".env"


settings = Settings()
