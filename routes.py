from fastapi import APIRouter

from controllers.users import router as users

routes = APIRouter()

routes.include_router(users, prefix='/users', tags=['users'])
