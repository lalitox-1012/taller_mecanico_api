from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base_datos.connection import Base

class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    telefono = Column(String(20))
    email = Column(String(100))

    vehiculos = relationship("Vehiculo", back_populates="cliente")