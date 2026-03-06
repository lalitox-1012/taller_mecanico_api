from pydantic import BaseModel

class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    placa: str


class VehiculoCreate(VehiculoBase):
    pass


class VehiculoResponse(VehiculoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True