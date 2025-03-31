from fastapi import *
from contextlib import asynccontextmanager
from db import create_tables, database, User


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def handle_database(request: Request, call_next):
    print("databse connect...")
    database.connect()
    response = await call_next(request)
    database.close()
    print("databse close...")
    return response


@app.get("/")
async def main():
    user = User()
    return user.followers()
