from fastapi import FastAPI
from base_datos.connection import engine, Base

from base_datos import cliente_model
from base_datos import vehiculo_model

from Presentacion.cliente_router import router as cliente_router
from Presentacion.vehiculo_router import router as vehiculo_router
from Presentacion.orden_servicio_router import router as orden_router


app = FastAPI(title="API Taller Mecánico")

Base.metadata.create_all(bind=engine)

app.include_router(cliente_router)
app.include_router(vehiculo_router)
app.include_router(orden_router)


@app.get("/")
def root():
    return {"mensaje": "API Taller Mecánico funcionando"}