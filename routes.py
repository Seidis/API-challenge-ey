from fastapi import APIRouter

from controllers.users import router as users
from controllers.vagas import router as vagas
from controllers.cursos import router as cursos
from controllers.users_personal import router as users_personal
from controllers.candidatura import router as candidatura
from controllers.insignias import router as insignias

routes = APIRouter()

routes.include_router(users, prefix='/users', tags=['users'])
routes.include_router(
    users_personal, prefix='/users_personal', tags=['users_personal'])
routes.include_router(vagas, prefix='/vagas', tags=['vagas'])
routes.include_router(cursos, prefix='/cursos', tags=['cursos'])
routes.include_router(candidatura, prefix='/candidatura', tags=['candidatura'])
routes.include_router(insignias, prefix='/insignias', tags=['insignias'])
