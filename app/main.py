from fastapi import FastAPI
from app.api.usuarios import routes as user_routes
from app.api.auth import routes as auth_routes
from app.api.equipos import routes as equipos_routes
from app.api.areas import routes as areas_routes
from app.db.database import Base, engine

# Crear tablas (solo para pruebas o desarrollo)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestión IT",
    version="1.0.0"
)

# Incluir rutas
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
app.include_router(equipos_routes.router)
app.include_router(areas_routes.router)