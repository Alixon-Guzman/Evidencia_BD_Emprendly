from db import Base

from sqlalchemy import Date, Column, Integer, String, ForeignKey

from datetime import datetime


class Ventas(Base):
    __tablename__= "ventas"
    id = Column (Integer , primary_key=True)
    valor= Column (String(100))
    cantidad= Column (String(100))
    fecha_registro = Column(Date, default=datetime.now())
    Usuarios_id = Column(Integer, ForeignKey("usuarios.id"))
