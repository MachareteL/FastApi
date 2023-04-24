from typing import Optional
from pydantic import BaseModel as SchemaBaseModel
#Como o SQL Alchemy tem o BaseModel dele, não poderemos confundir...
class CursoSchema(SchemaBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    instrutor: str
    class Config:
        orm_mode = True
