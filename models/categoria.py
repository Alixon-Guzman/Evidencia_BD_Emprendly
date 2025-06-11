#importar modelo base 
from db import Base 

#importaciones 
from sqlalchemy import Column, Integer, String 

class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
