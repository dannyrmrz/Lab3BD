# filepath: c:\Users\BRUTE\Documents\GitHub\Lab3BD\backend\app\custom_types.py

from enum import Enum

class TipoUsuario(str, Enum):
    visitante = "visitante"
    empleado = "empleado"

class EstadoReserva(str, Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"
    cancelada = "cancelada"