from typing import Optional
from pydantic import BaseModel


class BaseCurso(BaseModel):
    id: int = None
    title: str = None
    image: str = None
    description: str = None
    tipo: str = None

    class Config:
        orm_mode = True


class BaseCursoAtivo(BaseModel):
    id: int = None
    user_id: int = None
    curso_ativo: int = None
    aula_ativa: int = None

    class Config:
        orm_mode = True
