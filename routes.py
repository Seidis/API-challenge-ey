from fastapi import APIRouter

from controllers.users import router as users
from controllers.vagas import router as vagas
from controllers.cursos import router as cursos

routes = APIRouter()

routes.include_router(users, prefix='/users', tags=['users'])
routes.include_router(vagas, prefix='/vagas', tags=['vagas'])
routes.include_router(cursos, prefix='/cursos', tags=['cursos'])
