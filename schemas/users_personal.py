from datetime import date
from typing import Optional
from pydantic import BaseModel

class UserPersonal(BaseModel):
    id: int = None
    user_id: int
    nome_social: str
    cpf: str
    telefone: str
    data_nascimento: date

    class Config:
        orm_mode = True

class UserPersonalPatch(BaseModel):
    nome_social: Optional[str]
    cpf: Optional[str]
    telefone: Optional[str]
    data_nascimento: Optional[date]