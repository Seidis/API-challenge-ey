from fastapi import APIRouter
from fastapi_sqlalchemy import db

from models.users import User as ModelUser
from schemas.users import User, CreateUser

router = APIRouter()


@router.get('/', response_model=list[User])
async def users():
    users = db.session.query(ModelUser).all()
    return users


@router.post('/', response_model=CreateUser)
async def create_user(user: CreateUser):
    new_user = ModelUser(**user.dict())
    db.session.add(new_user)
    db.session.commit()
    return new_user
