from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_v1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/etscursos'
    DB_BaseModel = declarative_base()
    class Config:
        case_sensitive = True
settings = Settings()
