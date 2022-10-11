import os
import sys
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
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "challenge-ey.web.app",
    "challenge-ey.firebaseapp.com"
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
    try:
        await config.database.connect()
    except Exception as e:
        print('Erro ao conectar ao banco de dados')


@app.on_event("shutdown")
async def shutdown() -> None:
    await config.database.disconnect()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(routes, prefix='')
