from typing import Optional
# pyrefly: ignore [missing-import]
from pydantic import BaseModel


class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int = 0


class ProductoCreate(ProductoBase):
    pass


class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True