from pydantic import BaseModel
from typing import List, Optional
from datetime import time

class ReservaBase(BaseModel):
    id_usuario: int
    id_cola: int
    estado: str
    hora_reserva: time

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(ReservaBase):
    estado: Optional[str] = None
    hora_reserva: Optional[time] = None

class Reserva(ReservaBase):
    id_reserva: int

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    tipo_usuario: str

class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True

class AtraccionBase(BaseModel):
    nombre: str
    descripcion: str
    capacidad: int
    tiempo_promedio: int

class Atraccion(AtraccionBase):
    id_atraccion: int

    class Config:
        orm_mode = True

class ColaBase(BaseModel):
    id_atraccion: int
    fecha: str
    max_personas: int

class Cola(ColaBase):
    id_cola: int

    class Config:
        orm_mode = True