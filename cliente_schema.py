from pydantic import BaseModel
from typing import Optional
from servicios.vehiculo_schema import VehiculoCreate

class ClienteCreate(BaseModel):
    nombre: str
    telefono: str
    email: str
    vehiculo: Optional[VehiculoCreate] = None


class ClienteResponse(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str

    class Config:
        from_attributes = True