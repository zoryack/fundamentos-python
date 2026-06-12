#  Backend API de Inventario con FastAPI y SQLite

¡Bienvenido! Este proyecto es un sistema de gestión de inventario para videojuegos desarrollado en **Python**, estructurado como una API REST funcional con persistencia en base de datos relacional. 

Diseñado siguiendo las mejores prácticas de desarrollo backend para perfiles de ingeniería de software.

##  Tecnologías Utilizadas

* **Python 3** (Lógica central del sistema)
* **FastAPI** (Framework web asíncrono de alto rendimiento)
* **Uvicorn** (Servidor ASGI local)
* **SQLite3** (Motor de base de datos relacional ligero)
* **Pydantic** (Validación de estructuras de datos y esquemas)
* **Git & GitHub** (Control de versiones y documentación)

---

##  Arquitectura y Características

El proyecto implementa un flujo de arquitectura limpia, dividiendo la capa de inicialización de datos de la capa de rutas web:

1. Persistencia Real: Los datos no se almacenan en memoria RAM; se registran de forma permanente en un archivo binario `.db` mediante sentencias SQL.
2. Validación Estricta: Uso de modelos de Pydantic para garantizar que las peticiones entrantes tengan el formato adecuado antes de interactuar con la base de datos.
3. Control de Entorno: Configuración de `.gitignore` para omitir archivos compilados (`__pycache__`) y bases de datos de prueba locales.

---

##  Endpoints de la API

La API cuenta con los siguientes puntos de acceso (pueden ser testeados localmente mediante herramientas como Thunder Client):

### 1. Obtener Inventario
* **Método:** `GET`
* **Ruta:** `/inventario`
* **Descripción:** Conecta con SQLite, extrae todos los ítems registrados y los retorna estructurados en una lista de formato JSON.

### 2. Agregar Ítem Dinámico
* **Método:** `POST`
* **Ruta:** `/items`
* **Descripción:** Recibe un cuerpo JSON con el molde exigido (`nombre` y `cantidad`) e inyecta de forma segura el nuevo registro en la tabla SQL mediante parámetros enlazados.