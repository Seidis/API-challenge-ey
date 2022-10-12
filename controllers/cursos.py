from typing import List
from config import database
from fastapi import APIRouter, HTTPException

from schemas.cursos import BaseCurso

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
