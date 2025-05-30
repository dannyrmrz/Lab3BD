

from enum import Enum

class TipoUsuario(str, Enum):
    visitante = "visitante"
    empleado = "empleado"

class EstadoReserva(str, Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"
    cancelada = "cancelada"