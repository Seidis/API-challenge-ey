import datetime
from pydantic import BaseModel
        
class User(BaseModel):
    name: str = None
    tax_id: str = None
    telephone: str = None
    birth_date: datetime.date = None
    username: str = None
    password: str = None
    email: str = None
    role: str = None

    class Config:
        orm_mode = True