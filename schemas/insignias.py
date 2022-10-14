from pydantic import BaseModel


class BaseInsignia(BaseModel):
    id: int = None
    user_id: int = None
    insignia_id: int = None
    opened: bool = False

    class Config:
        orm_mode = True
