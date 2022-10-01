import databases
import sqlalchemy
import os

from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.environ['DATABASE_URL']
database = databases.Database(BASE_URL)
metadata = sqlalchemy.MetaData()


async def connect():
    await database.connect()
    return 'Connected to database'
