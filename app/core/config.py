from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    TITLE: str
    SECRET: str

    DEPOSIT: str = "DEPOSIT"
    WITHDRAW: str = "WITHDRAW"

    DB_PORT: int
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def date_base(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
