import os
import config
from routes import routes
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title='Challenge EY - API',
              description='API para o desafio da EY',
              version='1.0.0')


@app.on_event("startup")
async def startup() -> None:
    await config.database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await config.database.disconnect()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(routes, prefix='')
