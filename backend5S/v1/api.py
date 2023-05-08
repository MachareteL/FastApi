from fastapi import APIRouter
from v1.endpoints.curso import router

api_router = APIRouter()
api_router.include_router(router, prefix='/cursos', tags=["cursos"])
#/api/v1/cursos -> esse será nosso endpoint completo junto ao prefixo!


