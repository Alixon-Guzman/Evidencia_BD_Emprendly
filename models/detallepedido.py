from db import Base 

from sqlalchemy import Column, Integer, String, ForeignKey



class Detallepedido(Base):
       __tablename__ = "detalle_pedido"
    id = Column(Integer, primary_key=True)
    ventas_id = Column(Integer, ForeignKey("ventas.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))
 