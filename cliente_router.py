from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from servicios.cliente_schema import ClienteCreate, ClienteResponse
from logica_negocio import cliente_service
from base_datos.connection import get_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/", response_model=ClienteResponse)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.crear_cliente(db, cliente)