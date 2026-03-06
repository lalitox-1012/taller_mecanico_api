from sqlalchemy.orm import Session
from base_datos.vehiculo_model import Vehiculo

def crear_vehiculo(db: Session, vehiculo_data, cliente_id: int):
    nuevo_vehiculo = Vehiculo(
        marca=vehiculo_data.marca,
        modelo=vehiculo_data.modelo,
        placa=vehiculo_data.placa,
        cliente_id=cliente_id
    )

    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)

    return nuevo_vehiculo