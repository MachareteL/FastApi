__author__ = "Lucas Macharete"
__version__ = 1.0
'''
    Last_Modified: 27/03/2022
    Last_Updates : {
        1:{
        Typing variables and add docummentation.
        }
    }

'''


# from fastapi import FastAPI, Response
# import json
# from typing import Optional

from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()





from fastapi import FastAPI
from core.configs import settings
from v1.api import api_router

app = FastAPI(title='API de Cursos da ETS')
app.include_router(api_router, prefix=settings.API_v1_STR)







origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)


# @app.get("/alunos")
# async def get_alunos():
#     '''
#     Fetch this endpoint to retrieve all ETS Students list
#     Return : JSON
#     '''
#     with open("./tabelas/alunos.txt") as arquivo:
#         data = json.load(arquivo)
#         return data
    

# @app.get("/")
# async def root():
#     with open('./alunos/NOMES.json', 'r') as alunos:
#         lista_alunos = alunos.read()
#         print(lista_alunos)
#         alunos.close()
#     return Response(content=lista_alunos, status_code=200)

# @app.post('/{nome}')
# async def root_post(nome : str, idade : Optional[int] = 0) -> dict:
#     ''' Post a name and an age to print it on terminal '''
#     print(nome)
#     return Response(content="Post Root", status_code=202)

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)