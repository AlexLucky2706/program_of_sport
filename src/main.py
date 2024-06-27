from fastapi import FastAPI
from uvicorn import run
from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate
from program.router import router as router_program
from result.router import router as router_result
from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend
from config import REDIS_HOST, REDIS_PORT
from fastapi_cache import FastAPICache
from tasks.router import router as router_tasks

app = FastAPI(title='Training')

app.include_router(router_program)
app.include_router(router_result)
app.include_router(router_tasks)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)



@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == '__main__':
    run(app)