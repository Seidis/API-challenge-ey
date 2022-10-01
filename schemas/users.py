import datetime
from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int = None
    name: str = None
    email: str = None
    password: str = None
    role: str = None

    class Config:
        orm_mode = True


class UserData(BaseUser):
    cpf: str = None
    telephone: str = None
    birth_date: datetime.date = None

    class Config:
        orm_mode = True
