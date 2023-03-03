from databases import Database
import aioredis
from config import settings


redis = None

db = Database(settings.POSTGRES_URL)

def get_db():
    return db


async def connect_to_redis():
    global redis
    redis = await aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    #redis = await aioredis.from_url(f"redis://localhost:{settings.REDIS_PORT}")

async def disconnect_from_redis():
    await redis.close()




