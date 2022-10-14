from typing import List
from config import database
from fastapi import APIRouter, HTTPException

from schemas.cursos import BaseCurso, BaseCursoAtivo

router = APIRouter()


@router.get("/", response_model=List[BaseCurso])
async def get_all_cursos():
    sql = """
        SELECT * FROM cursos
    """
    return await database.fetch_all(sql)


@router.get("/{id}", response_model=BaseCurso)
async def get_curso(id: int):
    sql = f"""
        SELECT * FROM cursos WHERE id = { id }
    """
    return await database.fetch_one(sql)


@router.post("/")
async def create_curso(curso: BaseCurso):
    sql = f"""
        INSERT INTO cursos (title, image, description, tipo)
        VALUES ('{curso.title}', '{curso.image}', '{curso.description}', '{curso.tipo}')
    """
    db_curso = await database.fetch_one(sql)

    return db_curso


@router.get("/ativos/{id}", response_model=List[BaseCursoAtivo])
async def get_cursos_ativos(id: int):
    sql = f"""
        SELECT * FROM cursos_ativos WHERE user_id = { id }
    """
    return await database.fetch_all(sql)


@router.get("/last_ativo/{id}")
async def get_last_curso_ativo(id: int):
    sql = f"""
        SELECT 
            c.id AS id_curso,
            c.title,
            c.tipo,
            ca.id,
            ca.user_id,
            ca.curso_ativo,
            ca.aula_ativa
        FROM cursos c 
        LEFT JOIN cursos_ativos ca ON c.id = ca.curso_ativo 
        WHERE ca.user_id = { id }
        ORDER BY ca.id DESC LIMIT 1
    """

    db_req = await database.fetch_one(sql)
    return {
        "id": db_req["id"],
        "user_id": db_req["user_id"],
        "curso_ativo": db_req["curso_ativo"],
        "aula_ativa": db_req["aula_ativa"],
        "id_curso": db_req["id_curso"],
        "title": db_req["title"],
        "tipo": db_req["tipo"]
    }


@router.post("/ativos/")
async def create_curso_ativo(curso_ativo: BaseCursoAtivo):
    sql = f"""
        INSERT INTO cursos_ativos (user_id, curso_ativo, aula_ativa)
        VALUES ({curso_ativo.user_id}, {curso_ativo.curso_ativo}, {curso_ativo.aula_ativa})
    """
    db_curso_ativo = await database.fetch_one(sql)

    return db_curso_ativo
