from config import database

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from controllers.depends.users import get_usuario_logado
from models.users import User

from schemas.users import BaseUser, CreateUser, UserData, UserLogin
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
        'token_type': 'bearer'
    }


@router.get('/data', response_model=List[UserData])
async def get_all_users_data():
    sql = """
        SELECT * from users
        LEFT JOIN users_data ON users.id = users_data.user_id
        WHERE users.id = users_data.user_id
    """
    return await database.fetch_all(sql)


@router.get('/data/{id}', response_model=UserData)
async def get_user_data(id: int):
    sql = f"""
        SELECT * from users
        LEFT JOIN users_data ON users.id = users_data.user_id
        WHERE user_id = {id}
    """
    return await database.fetch_one(sql)


@router.patch('/{id}', response_model=UserData)
async def update_user_data(id: int, user_data: UserData):

    for key, value in user_data.dict().items():
        if value is not None:
            sql = f"""
                UPDATE users_data
                SET {key} = '{value}'
                WHERE user_id = {id}
            """
            await database.execute(sql)

    return await get_user_data(id)


@router.post("/", response_model=UserData)
async def register_user(user: CreateUser):

    data = user.dict()

    sql = f"""
        INSERT INTO users (name, email, password, role)
        VALUES ('{data['name']}', '{data['email']}', '{data['password']}', '{data['role']}')
    """
    await database.execute(sql)

    return user


@router.delete('/{id}')
async def delete_user(id: int):
    sql = f"""
        DELETE FROM users_data
        WHERE user_id = {id}
    """
    await database.execute(sql)

    sql = f"""
        DELETE FROM users
        WHERE id = {id}
    """
    await database.execute(sql)

    return {'message': 'User deleted successfully'}
