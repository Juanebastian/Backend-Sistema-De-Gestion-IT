from fastapi import FastAPI
from app.api.usuarios import routes as user_routes
from app.api.auth import routes as auth_routes
from app.api.equipos import routes as equipos_routes
from app.api.areas import routes as areas_routes
from app.api.tickets import routes as tickets_routes
from app.api.marcas import routes as marcas_routes
from app.db.database import Base, engine
from app.api.modelos import routes as modelos_routes
from app.api.sistemas_operativos import routes as sistemas_operativos_routes
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
app.include_router(tickets_routes.router)
app.include_router(marcas_routes.router)
app.include_router(modelos_routes.router)
app.include_router(sistemas_operativos_routes.router)