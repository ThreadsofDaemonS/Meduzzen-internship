from databases import Database
import asyncio
import aioredis
from config import settings


#DATABASE_URL=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
DATABASE_URL=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@database:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
database = Database(DATABASE_URL)

async def ConnectionToDbs():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    #redis = aioredis.from_url(f"redis://localhost:{settings.REDIS_PORT}")
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
    print(value)



if __name__ == "__main__":
    asyncio.run(ConnectionToDbs())


