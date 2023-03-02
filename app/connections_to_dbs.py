from databases import Database
import aioredis
from config import settings


#DATABASE_URL=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
DATABASE_URL=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@database:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
database = Database(DATABASE_URL)

def ConnectionToDb():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    #redis = aioredis.from_url(f"redis://localhost:{settings.REDIS_PORT}")





