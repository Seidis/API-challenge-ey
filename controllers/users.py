from config import database

from typing import List
from fastapi import APIRouter, HTTPException

from schemas.users import AllUserData, BaseUser, CreateUser, UserData
from security import criar_token_jwt, verify_password

router = APIRouter()


@router.get('/', response_model=List[BaseUser])
async def get_all_users():
    sql = """
        SELECT * FROM users
    """
    return await database.fetch_all(sql)


@router.get('/{id}', response_model=BaseUser)
async def get_user(id: int):
    sql = f"""
        SELECT * FROM users WHERE id = {id}
    """
    user = await database.fetch_one(sql)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post('/login')
async def login_user(user: str, password: str):
    sql = f"""
        SELECT * FROM users WHERE email = '{user}'
    """
    db_user = await database.fetch_one(sql)
    if not db_user or not verify_password(password, db_user['password']):
        raise HTTPException(status_code=403, detail='User not found')
    return {
        'id': db_user['id'],
        'access_token': criar_token_jwt(db_user['id']),
        'role': db_user['role'],
        'token_type': 'bearer'
    }


@router.post("/", response_model=BaseUser)
async def register_user(user: CreateUser):

    data = user.dict()

    sql = f"""
        INSERT INTO users (name, surname, email, password, role)
        VALUES ('{data['name']}', '{data['surname']}','{data['email']}', '{data['password']}', '{data['role']}')
    """
    await database.execute(sql)

    return user


@router.get('/all/{id}', response_model=AllUserData)
async def get_all_user_data(id: int):
    sql = f"""
        SELECT * FROM users
        LEFT JOIN users_personal ON users.id = users_personal.user_id
        WHERE users.id = {id}
    """
    return await database.fetch_one(sql)