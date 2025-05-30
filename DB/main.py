from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable
from database import Base
from models import Usuario, Atraccion, Cola, Reserva  # importa modelos
from sqlalchemy.dialects import postgresql

# Conexión a tu base de datos
engine = create_engine("postgresql://javiercarredano:nievedelimon@localhost:5432/Laboratorio3")

# Crea las tablas y enums en la base
Base.metadata.create_all(engine)



# Exportar schema.sql con contenido real
def export_schema(engine, filename='schema.sql'):
    with open(filename, 'w') as f:
        for table in Base.metadata.sorted_tables:
            f.write(str(CreateTable(table).compile(engine)) + ';\n\n')
        
# Llama a la función para exportar el esquema
export_schema(engine, 'schema.sql')

