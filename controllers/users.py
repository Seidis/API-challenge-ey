from config import database

from typing import List
from fastapi import APIRouter

from schemas.users import BaseUser as BaseUserSchema
from schemas.users import UserData as UserDataSchema

router = APIRouter()


@router.get('/', response_model=List[BaseUserSchema])
async def get_all_users():
    sql = 'SELECT * FROM users'
    return await database.fetch_all(sql)


@router.get('/data', response_model=List[UserDataSchema])
async def get_all_users_data():
    sql = """
        SELECT * from users
        LEFT JOIN users_data ON users.id = users_data.user_id
        WHERE users.id = users_data.user_id
    """
    return await database.fetch_all(sql)


@router.get('/{id}', response_model=UserDataSchema)
async def get_user_data(id: int):
    sql = f"""
        SELECT * from users
        LEFT JOIN users_data ON users.id = users_data.user_id
        WHERE user_id = {id}
    """
    return await database.fetch_one(sql)


@router.patch('/{id}', response_model=UserDataSchema)
async def update_user_data(id: int, user_data: UserDataSchema):

    for key, value in user_data.dict().items():
        if value is not None:
            sql = f"""
                UPDATE users_data
                SET {key} = '{value}'
                WHERE user_id = {id}
            """
            await database.execute(sql)

    return await get_user_data(id)
