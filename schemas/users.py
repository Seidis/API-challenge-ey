from lib2to3.pgen2 import token
from pydantic import BaseModel, validator
import datetime

from security import get_password_hash


class BaseUser(BaseModel):
    id: int = None
    name: str = None
    surname: str = None
    email: str = None
    role: str = None

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    password: str

    @validator('password', pre=True, check_fields=False)
    def hash_password(cls, v):
        return get_password_hash(v)


class UserData(BaseUser):
    cpf: str = None
    telephone: str = None
    birth_date: datetime.date = None

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    id: int
    acess_token: str
    token_type: str
