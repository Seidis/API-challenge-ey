from pydantic import BaseModel


class BaseCandidatura(BaseModel):
    id: int = None
    job_id: int = None
    candidate_id: int = None

    class Config:
        orm_mode = True
