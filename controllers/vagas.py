from http.client import HTTPException
from config import database
from fastapi import APIRouter
from typing import List

from schemas.vagas import BaseVaga

router = APIRouter()


@router.get('/', response_model=List[BaseVaga])
async def get_all_vagas():
    sql = """
        SELECT * FROM vagas
    """
    return await database.fetch_all(sql)


@router.get('/ativas', response_model=List[BaseVaga])
async def get_vagas_ativas():
    sql = """
        SELECT * FROM vagas WHERE is_active = True
    """
    return await database.fetch_all(sql)


@router.get('/{id}', response_model=BaseVaga)
async def get_vaga(id: int):
    sql = f"""
        SELECT * FROM vagas WHERE id = {id}
    """
    vaga = await database.fetch_one(sql)
    if not vaga:
        raise HTTPException(status_code=404, detail="Vaga not found")
    return vaga


@router.post('/', response_model=BaseVaga)
async def create_vaga(vaga: BaseVaga):
    sql = f"""
        INSERT INTO vagas (
            image_url,
            title,
            short_description,
            description,
            salary,
            location,
            type,
            level,
            created_on,
            is_active,
            expire_date
            )
        VALUES (
            '{vaga.image_url}',
            '{vaga.title}',
            '{vaga.short_description}',
            '{vaga.description}',
            {vaga.salary},
            '{vaga.location}',
            '{vaga.type}',
            '{vaga.level}',
            CURRENT_TIMESTAMP,
            {vaga.is_active},
            '{vaga.expire_date}'
            )
    """
    await database.execute(sql)
    return vaga


@router.patch('/{id}', response_model=BaseVaga)
async def update_vaga(id: int, vaga: BaseVaga):

    data = vaga.dict(exclude_unset=True)

    for key, value in data.items():
        sql = f"""
            UPDATE vagas
            SET {key} = '{value}'
            WHERE id = {id}
        """
        await database.execute(sql)

    return vaga