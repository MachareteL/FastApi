import sys
core_path = sys.path[0][:-7]
sys.path.append(core_path)

from core.configs import settings
from sqlalchemy import Column, Integer, String

#DBBaseModel é a classe declarativa do SQl Alchemy
class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    título: str = Column(String(100))
    horas: int = Column(Integer)
    aulas: int = Column(Integer)
    instrutor: str = Column(String(100))