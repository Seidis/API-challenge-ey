from fastapi import APIRouter
from fastapi_sqlalchemy import db

from models.users import User as ModelUser
from schemas.users import User as SchemaUser

router = APIRouter()


@router.get('/', response_model=list[SchemaUser])
async def users():
    users = db.session.query(ModelUser).all()
    return users
