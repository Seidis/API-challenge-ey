from typing import List
from fastapi import APIRouter
from config import database

from schemas.users_personal import UserPersonal, UserPersonalPatch

router = APIRouter()

@router.get('/', response_model=List[UserPersonal])
async def get_user_personal():
    sql = """
        SELECT * FROM users_personal
    """
    return await database.fetch_all(sql)


@router.get('/{id}')
async def get_user_personal(id: int):
    sql = f"""
        SELECT up.* FROM users_personal up
        LEFT JOIN users u ON u.id = up.user_id
        WHERE u.id = {id}
    """
    db_user = await database.fetch_one(sql)

    if not db_user:
        return False

    return True


@router.post('/create')
async def create_user_personal(user_personal: UserPersonal):
    sql = f"""
        INSERT INTO users_personal (user_id, nome_social, cpf, telefone)
        VALUES ({user_personal.user_id}, '{user_personal.nome_social}', '{user_personal.cpf}', '{user_personal.telefone}')
    """
    db_user_personal = await database.fetch_one(sql)

    return db_user_personal

@router.patch('/update/{id}')
async def update_user_personal(id: int, user_personal: UserPersonalPatch):

    data = user_personal.dict(exclude_unset=True)

    for key, value in data.items():
        sql = f"""
            UPDATE users_personal
            SET {key} = '{value}'
            WHERE user_id = {id}
        """
        await database.execute(sql)