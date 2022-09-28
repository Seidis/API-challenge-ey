from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from routes.users import router as users_router


import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title='Challenge EY - API',
              description='API para o desafio da EY',
              version='1.0.0')

origins = [
    "http://localhost",
    "http://localhost:3000",
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

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(users_router, prefix='/users', tags=['users'])
