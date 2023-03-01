from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST: str
    PORT: int
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str

    POSTGRES_PORT: int

    REDIS_HOST: str
    REDIS_URL: str
    REDIS_PORT: int

    DEBUG = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

#print(settings)