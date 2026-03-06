from pydantic import BaseModel
from datetime import date

class OrdenServicioBase(BaseModel):
    descripcion: str
    fecha: date
    costo: float
    vehiculo_id: int

class OrdenServicioCreate(OrdenServicioBase):
    pass

class OrdenServicioResponse(OrdenServicioBase):
    id: int

    class Config:
        from_attributes = True