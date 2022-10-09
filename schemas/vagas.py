from datetime import date
from pydantic import BaseModel, validator


class BaseVaga(BaseModel):
    id: int = None
    image_url: str = None
    title: str = None
    short_description: str = None
    description: str = None
    salary: float = None
    location: str = None
    type: str = None
    level: str = None
    is_active: bool = True
    expire_date: date = None

    class Config:
        orm_mode = True
