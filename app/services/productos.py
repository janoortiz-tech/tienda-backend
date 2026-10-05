from sqlalchemy.orm import Session
from typing import Optional
from app import models, schemas

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    # Convertimos el schema de Pydantic a un modelo SQLAlchemy
    db_producto = models.Producto(**producto.model_dump()) 
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def listar_productos(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    nombre: Optional[str] = None, 
    precio_max: Optional[float] = None
):
    query = db.query(models.Producto)
    
    # Filtro por nombre (búsqueda parcial insensible a mayúsculas/minúsculas)
    if nombre:
        query = query.filter(models.Producto.nombre.ilike(f"%{nombre}%"))
        
    # Filtro por precio máximo
    if precio_max is not None:
        query = query.filter(models.Producto.precio <= precio_max)
        
    # Aplicar paginación (skip y limit)
    return query.offset(skip).limit(limit).all()