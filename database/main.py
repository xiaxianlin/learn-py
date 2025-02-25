from fastapi import *
from contextlib import asynccontextmanager
from db import create_tables, database


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def handle_database(request: Request, call_next):
    database.connect()
    response = await call_next(request)
    database.close()
    return response
