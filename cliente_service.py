from sqlalchemy.orm import Session
from persistencia import cliente_repository, vehiculo_repository

def crear_cliente(db: Session, cliente_data):

    # crear cliente
    nuevo_cliente = cliente_repository.crear_cliente(db, cliente_data)

    # crear vehiculo si viene
    if cliente_data.vehiculo:
        vehiculo_repository.crear_vehiculo(
            db,
            cliente_data.vehiculo,
            nuevo_cliente.id
        )

    return nuevo_cliente