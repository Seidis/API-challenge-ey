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
