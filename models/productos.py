from db import Base 

from sqlalchemy import Column, Integer, String, ForeignKey


class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    modelo =Column(String(60))
    precio_unitario = Column(String(60))
    fecha_registro = Column(String(60))
    categoria_id = Column(Integer,
            ForeignKey("categorias.id"))