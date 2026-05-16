from faker import Faker
from database import engine, SessionLocal
from models import Base, Usuario
from sqlalchemy import text, insert


def main() -> None:
# Implementación de generación automática de datos para poblar la base de datos
    fake = Faker('es_ES')

    # Crear tabla automáticamente
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    # Limpiar tabla
    session.query(Usuario).delete()
    session.commit()

    # limpiar registros anteriores y reiniciar el autoincremento 
    session.execute(text("ALTER TABLE personas_sofia AUTO_INCREMENT = 1"))
    session.commit()

    rows = [
        {
            "nombre": fake.name(),
            "apellido": fake.last_name(),
            "correo": fake.email(),
            "telefono": fake.phone_number(),
            "ciudad": fake.city(),
            "direccion": fake.address(),
            "fecha_nacimiento": str(fake.date_of_birth()),
            "empresa": fake.company()
        }
        for _ in range(100000)
    ]

    #inserción masiva con execute()
    session.execute(insert(Usuario), rows)
    session.commit()

    print("Insertaste los datos correctamente")


if __name__ == "__main__":
    main()
