from sqlalchemy.orm import Session
from base_datos.cliente_model import Cliente

def crear_cliente(db: Session, cliente):
    nuevo_cliente = Cliente(
        nombre=cliente.nombre,
        telefono=cliente.telefono,
        email=cliente.email
    )

    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)

    return nuevo_cliente