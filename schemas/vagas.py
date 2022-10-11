from datetime import date
from tokenize import group
from typing import Optional
from pydantic import BaseModel


class BaseVaga(BaseModel):
    id: int = None
    image_url: str = None
    title: str = None
    short_description: str = None
    description: str = None
    salary: float = None
    city: str = None
    state: str = None
    type: str = None
    level: str = None
    is_active: bool = True
    expire_date: date = None
    tecnical: bool = False
    personal: bool = False
    group_event: bool = False
    first_interview: bool = False
    final_interview: bool = False
    tecnical_date: Optional[date]
    personal_date: Optional[date]
    group_date: Optional[date]
    first_interview_date: Optional[date]
    final_interview_date: Optional[date]

    class Config:
        orm_mode = True
