from db import Base
from sqlalchemy import Enum, Column, Integer, String, ForeignKey
from models.enums import Tipodocumento

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    apellido = Column(String(40))
    correo = Column(String(100))
    contraseña = Column(String(40))
    rol = Column(String(60))
    numero_documento = Column(Integer)
    tipo_documento = Column(Enum(Tipodocumento))
