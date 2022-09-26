# build a schema using pydantic
import datetime
from pydantic import BaseModel
        
class User(BaseModel):
    name: str = None
    tax_id: str = None
    telephone: str = None
    birth_date: datetime.datetime = None
    username: str = None
    password: str = None
    email: str = None
    role: str = None

    class Config:
        orm_mode = True