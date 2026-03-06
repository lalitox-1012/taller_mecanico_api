from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from base_datos.connection import Base
from datetime import date

class OrdenServicio(Base):
    __tablename__ = "ordenes_servicio"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=False)
    fecha = Column(Date, default=date.today)
    costo = Column(Float, nullable=False)

    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))

    # Relación inversa
    vehiculo = relationship("Vehiculo", back_populates="ordenes")