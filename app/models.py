from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from app.db.database import Base


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    # Campos nuevos para la Clase 7
    hashed_password = Column(String, nullable=False)
    rol = Column(String, default="customer", nullable=False)
    acepto_tratamiento = Column(Boolean, nullable=False)
    fecha_consentimiento = Column(
        DateTime, default=datetime.utcnow, nullable=False
    ) 
    