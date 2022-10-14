from typing import List
from fastapi import APIRouter
from config import database

from schemas.insignias import BaseInsignia

router = APIRouter()


@router.get("/")
async def get_all_insignias():
    sql = """
        SELECT * FROM insignias
    """
    return await database.fetch_all(sql)


@router.post("/")
async def create_insignia(insignia: BaseInsignia):
    sql = f"""
        INSERT INTO insignias (user_id, insignia_id, opened)
        VALUES ({insignia.user_id}, '{insignia.insignia_id}', {insignia.opened})
    """
    db_insignia = await database.fetch_one(sql)

    return db_insignia


@router.get("/user/{user_id}", response_model=List[BaseInsignia])
async def get_insignias_unopened_by_user_id(user_id: int):
    sql = f"""
        SELECT * FROM insignias 
        WHERE user_id = { user_id }
        AND opened = false
    """
    return await database.fetch_all(sql)
