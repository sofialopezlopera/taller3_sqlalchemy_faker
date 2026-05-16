# Generación e Inserción Masiva de Datos con Python, SQLAlchemy y Faker
## Descripción General

El presente proyecyo tiene como objetivo automatizar la creación y el poblado de una base de datos MYSQL mediante el uso de python. Para ello, se emplean librerías como SQLAlchemy para la conexion y manipulación de la base de datos, y Faker para la generación de registros ficticios, permitiendo simular informacion de manera eficiente y organizada 

El programa realiza todo el flujo sin intervención manual:

-Lee las credenciales desde variables de entorno.
-Se conecta a MySQL.
-Define la estructura de la tabla mediante ORM.
-Crea la tabla automáticamente si no existe.
-Genera 100.000 registros ficticios realistas.
-Inserta los datos de forma masiva y eficiente.


## Tecnologías Utilizadas

**Python**: Lenguaje principal del script
**SQLAlchemy**: Manejo de conexión y ORM
**Faker**: Generación automática de datos
**MySQL**: Sistema gestor de base de datos
**python-dotenv**: Carga segura de credenciales
**DBeaver**: Verificación de resultados
**Git & GitHub**: Control de versiones

## Estructura del Proyecto
```
taller3/
│
├── main.py
├── database.py
├── models.py
├── .env
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md
```
Cada archivo cumple una responsabilidad específica dentro del sistema de las que hablaremos más adelante.

## Configuración de Seguridad

**Archivo .env**

Contiene la conexión real a la base de datos:
```
DATABASE_URL=mysql+pymysql://root:tu_password@localhost:3306/taller3
```
Este archivo no se sube al repositorio, debido a que contiene información confidencial y credenciales sensibles que podrían comprometer la seguridad del sistema. Su exposición en un entorno público o compartido representaría un riesgo significativo, ya que terceros podrían acceder a datos de autenticación. Por esta razón, se recomienda mantenerlo únicamente en el entorno local

**Archivo .env.example**

El archivo funciona como una plantilla de configuración para otros usuarios que quieran ejecutar el proyecto en su propio entorno. En este archivo se definen las variables de entorno necesarias para el correcto funcionamiento de la aplicación, pero con valores ficticios o genéricos en lugar de información real.
```
DATABASE_URL=mysql+pymysql://tu_usuario:12345@localhost:3306/taller3
```
Este tipo de estructura permite indicar cómo debe construirse la conexión a la base de datos sin exponer credenciales reales como usuarios o contraseñas.

**Archivo .gitignore**

Es un componente fundamental dentro de un proyecto, ya que permite definir de manera explícita qué archivos y directorios deben ser ignorados por el sistema de control de versiones (Git). Su función principal es evitar que se suban al repositorio elementos que no son necesarios para el funcionamiento del proyecto o que pueden representar riesgos de seguridad o problemas de portabilidad.

En este caso, el archivo contiene las siguientes exclusiones:
```
.venv/
.env
__pycache__/
*.pyc
.DS_Store
```
Cada uno de estos elementos cumple un propósito específico:

- .venv/: evita que se suba el entorno virtual de Python, ya que este puede ser recreado fácilmente en cualquier máquina mediante el archivo de dependencias.
- .env: impide la subida de variables de entorno que suelen contener credenciales sensibles como contraseñas o configuraciones privadas.
- __pycache__/: excluye los archivos generados automáticamente por Python para la optimización del código.
- *.pyc: evita incluir archivos compilados de Python que no son necesarios para la ejecución del proyecto.
- .DS_Store: omite archivos ocultos generados por sistemas operativos como macOS, los cuales no aportan valor al proyecto.

**Archivo database.py**

Este archivo centraliza toda la conexión con MySQL.
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
```
1️. Carga de variables de entorno
```
load_dotenv()
```

Lee automáticamente el archivo .env para obtener la URL de conexión.

2️. Obtención de la cadena de conexión
```
DATABASE_URL = os.getenv("DATABASE_URL")
```
Extrae la variable DATABASE_URL sin escribir la contraseña directamente en el código.

3. Creación del engine
```
engine = create_engine(DATABASE_URL)
```
El engine es el objeto que administra:

-conexiones a MySQL
-ejecución de consultas
-manejo interno de transacciones

4️. Creación de sesiones
```
SessionLocal = sessionmaker(bind=engine)
```
Permite abrir sesiones para interactuar con la base de datos.

 Cada sesión representa una conexión activa.

**Definición del Modelo ORM**
**Archivo models.py**

Aquí se define la estructura de la tabla usando SQLAlchemy ORM.
```
Base = declarative_base()
```
La clase base en SQLAlchemy es un componente esencial dentro del sistema de mapeo objeto-relacional (ORM), ya que actúa como la estructura fundamental a partir de la cual se definen todas las entidades que serán representadas como tablas en la base de datos. Su función principal es establecer la relación entre las clases de Python y las tablas SQL, permitiendo que cada clase del modelo sea interpretada como una entidad persistente dentro del sistema de almacenamiento.

Clase Usuario
```
class Usuario(Base):
```
Representa una tabla dentro de MySQL.

```
__tablename__ = "personas_sofia"
```
Indica el nombre real de la tabla en la base de datos.

Columnas

```
nombre = Column(String(100))
```
Esto significa:

se crea una columna llamada nombre
tipo VARCHAR(100) en MySQL

El ORM convierte automáticamente la clase Python en:
```
CREATE TABLE personas_sofia (...)
```
 Por eso no es necesario escribir SQL manualmente.

## Script Principal
**Archivo main.py**

Este archivo ejecuta todo el flujo del proyecto.

Importaciones
```
from faker import Faker
from database import engine, SessionLocal
from models import Base, Usuario
from sqlalchemy import text, insert
````
Se importan:

El proyecto utiliza Faker para la generación de datos sintéticos que permiten simular información real de manera estructurada, facilitando así las pruebas y el poblamiento de la base de datos. Por otro lado, el engine se encarga de establecer y gestionar la conexión con la base de datos, actuando como el intermediario entre la aplicación y el motor de almacenamiento. Los modelos ORM definen la estructura de las entidades del sistema, permitiendo mapear clases de Python a tablas relacionales y simplificando la manipulación de los datos mediante programación orientada a objetos. Asimismo, se incorporan funciones SQL avanzadas que optimizan y complementan las operaciones sobre la base de datos, mejorando el rendimiento y la eficiencia de las consultas. Finalmente, la función principal def main() -> None: concentra toda la lógica del programa, coordinando la ejecución de los distintos componentes y asegurando el flujo correcto del proceso desde la generación de datos hasta su inserción en la base de datos.

Inicialización de Faker
fake = Faker('es_ES')

Configura Faker para generar datos en español:

-nombres reales
-direcciones válidas
-ciudades coherentes
-Creación automática de la tabla
```
Base.metadata.create_all(bind=engine)
```
SQLAlchemy verifica:

si la tabla existe → no hace nada
si no existe → la crea automáticamente

Esto permite ejecutar el script múltiples veces sin errores.

Apertura de sesión
```
session = SessionLocal()
```

Se abre una conexión activa con la base de datos.

Eliminación de registros anteriores

Antes de realizar la inserción de nuevos datos, el sistema ejecuta una limpieza de la tabla correspondiente con el objetivo de evitar inconsistencias o duplicados en la información cada vez que el programa es ejecutado. Para ello, se utiliza la instrucción:
```
session.query(Usuario).delete()
session.commit()
```
Esta operación elimina todos los registros existentes en la entidad asociada, asegurando que la base de datos se encuentre en un estado limpio y controlado antes de la generación de nuevos datos. Posteriormente, se realiza un commit que confirma de manera permanente los cambios efectuados sobre la base de datos.

Reinicio del AUTO_INCREMENT
```
session.execute(text("ALTER TABLE personas_sofia AUTO_INCREMENT = 1"))
session.commit()
```
Reinicia el contador del ID para comenzar nuevamente desde 1.

Generación masiva de datos
```
rows = [
    {...}
    for _ in range(100000)
]
```
Aquí ocurre la parte más importante.El programa genera 100.000 registros automáticamente usando Faker.Cada registro contiene:
-nombre
-apellido
-correo
-teléfono
-ciudad
-dirección
-fecha de nacimiento
-empresa
Esto simula información real de usuarios.

Inserción masiva optimizada

```
session.execute(insert(Usuario), rows)
session.commit()
```
En lugar de realizar la inserción de registros de manera individual, lo cual implica múltiples operaciones sobre la base de datos y puede afectar negativamente el rendimiento del sistema, se implementa una estrategia de inserción masiva de datos. Este enfoque permite agrupar los registros y enviarlos en una sola operación o en lotes optimizados, reduciendo significativamente la carga de trabajo del motor de base de datos.

La principal ventaja de esta técnica es la optimización del tiempo de ejecución, ya que disminuye el número de consultas realizadas. Además, se reduce el consumo de recursos tanto a nivel de memoria como de procesamiento, lo que contribuye a una ejecución más eficiente del programa. Como resultado, se obtiene un mejor rendimiento general del servidor, especialmente cuando se manejan grandes volúmenes de datos en entornos de pruebas o desarrollo.

El siguiente bloque de código define el punto de inicio de ejecución del script:
```
if __name__ == "__main__":
    main()
```
Esta estructura es una convención en Python que permite controlar cuándo un archivo debe ejecutarse como programa principal y cuándo debe ser importado como módulo dentro de otro archivo. De esta forma, la función main() solo se ejecuta cuando el script se lanza directamente desde la consola, evitando su ejecución automática en caso de ser reutilizado o importado en otro contexto.

Este mecanismo aporta orden y flexibilidad al proyecto, ya que separa claramente la lógica ejecutable principal del código reutilizable, facilitando su mantenimiento y escalabilidad.

Ejecutar el proyecto
```
python main.py
```
El programa:
- crea la tabla
- genera datos
- inserta 100.000 registros

**Instalación de Dependencias**
Instalar librerías necesarias:
```
pip install -r requirements.txt
```
Principales:
-SQLAlchemy
-Faker
-PyMySQL
-python-dotenv
-Verificación en DBeaver

Consulta utilizada:
```
SELECT COUNT(*) FROM personas_sofia;
```
Resultado esperado:
```
100000
```
Esto confirma que la inserción masiva fue exitosa.

## Resultados Obtenidos
-Creación automática de tablas desde Python.
-Implementación de ORM con SQLAlchemy.
-Generación masiva de datos simulados.
-Inserción eficiente de grandes volúmenes.
-Uso de variables de entorno para seguridad.
-Control de versiones con Git y GitHub.

Proyecto académico desarrollado con el objetivo de integrar y aplicar de manera práctica diversas tecnologías fundamentales en el desarrollo de software y la gestión de datos, combinando Python como lenguaje principal de programación con MySQL como sistema de gestión de bases de datos relacional. Adicionalmente, se emplea SQLAlchemy como herramienta de mapeo objeto-relacional (ORM), lo que permite una interacción más estructurada y eficiente con la base de datos, facilitando la manipulación de datos mediante objetos en lugar de consultas SQL directas.

Asimismo, se incorpora la librería Faker para la generación de datos sintéticos, lo que posibilita la creación de información ficticia pero coherente, ideal para entornos de prueba, desarrollo y validación del sistema sin comprometer datos reales. La integración de estas tecnologías permite construir un entorno completo que simula escenarios reales de trabajo, optimizando el proceso de diseño, pruebas e implementación de soluciones basadas en bases de datos.