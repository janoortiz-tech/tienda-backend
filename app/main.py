from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
import app.models

app = FastAPI()

# Crear las tablas en productos.db automáticamente
Base.metadata.create_all(bind=engine)

# Habilitar CORS para permitir peticiones desde React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import auth, productos

app.include_router(productos.router)
app.include_router(auth.router)