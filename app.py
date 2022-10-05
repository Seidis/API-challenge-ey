import os
import config
from routes import routes
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title='Challenge EY - API',
              description='API para o desafio da EY',
              version='1.0.0')

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    await config.database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await config.database.disconnect()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(routes, prefix='')
