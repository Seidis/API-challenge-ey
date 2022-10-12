from typing import List
from fastapi import APIRouter
from config import database

from schemas.candidatura import BaseCandidatura

router = APIRouter()


@router.get("/", response_model=List[BaseCandidatura])
async def get_candidaturas():
    sql = """
        SELECT * FROM candidaturas
    """
    return await database.fetch_all(sql)


@router.get("/{id}")
async def get_all_candidates(id: int):
    sql = f"""
        SELECT * FROM candidaturas WHERE job_id = {id}
    """
    candidates = await database.fetch_all(sql)

    return candidates


@router.post("/")
async def create_candidatura(candidatura: BaseCandidatura):
    sql = f"""
        INSERT INTO candidaturas (job_id, candidate_id)
        VALUES ({candidatura.job_id}, {candidatura.candidate_id})
    """
    await database.execute(sql)

    return candidatura


@router.get("/candidates/{id}")
async def get_all_candidates_2(id: int):
    sql = f"""
        SELECT 
            u.id,
            u."name",
            u.email,
            u.surname,
            up.nome_social,
            up.cpf,
            up.telefone,
            up.data_nascimento 
        FROM users u 
        LEFT JOIN users_personal up ON u.id = up.user_id 
        LEFT JOIN candidaturas c ON u.id = c.candidate_id 
        WHERE c.job_id = {id}
    """

    candidates = await database.fetch_all(sql)

    return candidates
