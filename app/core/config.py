from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TITLE: str = "Название проекта"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
