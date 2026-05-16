from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):

    __tablename__ = "personas_sofia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    nombre = Column(String(100))
    apellido = Column(String(100))
    correo = Column(String(150))
    telefono = Column(String(50))
    ciudad = Column(String(100))
    direccion = Column(String(200))
    fecha_nacimiento = Column(String(50))
    empresa = Column(String(150))    