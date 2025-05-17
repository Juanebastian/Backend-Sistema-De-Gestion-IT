from fastapi import FastAPI
from app.api.usuarios import routes as user_routes
from app.db.database import Base, engine

# Crear tablas (solo para pruebas o desarrollo)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestión IT",
    version="1.0.0"
)

# Incluir rutas
app.include_router(user_routes.router)
