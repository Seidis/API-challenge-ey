import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

# from models import User as ModelUser
# from schema import User as SchemaUser

from models.users import User as ModelUser
from schemas.users import User as SchemaUser

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get('/users/',response_model=list[SchemaUser])
async def users():
    users = db.session.query(ModelUser).all()
    return users

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)